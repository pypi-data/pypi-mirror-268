import os
import re
import csv
import logging
import requests
from tempfile import mkdtemp


def extract_notion_page_id(url):
    # Find URLs that starts with "https://www.notion.so" and extracts the UUID
    patterns = [
        r"https://www\.notion\.so/[^/]+/[^/]+-([a-f0-9]{32})",
        r"https://www\.notion\.so/[^/]+/([a-f0-9]{32})",
        r"https://www\.notion\.so/[^/]+-([a-f0-9]{32})",
        r"https://www\.notion\.so/([a-f0-9]{32})",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def extract_notion_page_ids(message):
    # "https://www.notion.so"で始まるURLを見つけてUUIDを抽出します
    patterns = [
        r"https://www\.notion\.so/[^/]+/[^/]+-([a-f0-9]{32})",
        r"https://www\.notion\.so/[^/]+/([a-f0-9]{32})",
        r"https://www\.notion\.so/[^/]+-([a-f0-9]{32})",
        r"https://www\.notion\.so/([a-f0-9]{32})",
    ]

    page_ids = []
    for pattern in patterns:
        matches = re.findall(pattern, message)
        if matches:
            page_ids.extend(matches)
    return page_ids


def markdown_to_notion_blocks(markdown_text):
    lines = markdown_text.split("\n")
    blocks = []
    current_indent_level = 0
    list_item_stack = [
        [] for _ in range(10)
    ]  # 10レベルのネストに対応するスタックを用意
    code_block_open = False
    code_language = ""
    code_content = []

    for line in lines:
        if (
            line.strip() == "" and not code_block_open
        ):  # 空行はスキップ（コードブロック外）
            continue

        # コードブロックの処理
        if line.startswith("```"):
            if code_block_open:  # コードブロックの終わり
                block = {
                    "object": "block",
                    "type": "code",
                    "code": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": "\n".join(code_content)},
                            }
                        ],
                        "language": code_language,
                    },
                }
                blocks.append(block)
                code_content = []
                code_block_open = False
                code_language = ""
            else:  # コードブロックの開始
                code_block_open = True
                code_language = line.strip("` ")
                # notionに対応した言語でない場合markdownに変換
                code_language = (
                    "markdown"
                    if code_language
                    not in [
                        "python",
                        "javascript",
                        "typescript",
                        "ruby",
                        "go",
                        "java",
                        "c",
                        "c++",
                        "c#",
                        "swift",
                        "kotlin",
                        "php",
                        "shell",
                        "sql",
                        "html",
                        "css",
                        "json",
                        "yaml",
                        "xml",
                        "markdown",
                        "plaintext",
                    ]
                    else code_language
                )
            continue

        if code_block_open:
            code_content.append(line)
            continue

        # 現在のインデントレベルを計算（スペース2つでインデント1つとする）
        indent_level = len(line) - len(line.lstrip(" "))
        indent_level //= 2  # 2スペースごとにインデントレベル1としてカウント

        # リンクの処理
        link_match = re.search(r"\[(.*?)\]\((.*?)\)", line)
        if link_match:
            text = link_match.group(1) or ""
            href = link_match.group(2) or ""
            if text and href.find("http") != -1:
                block = {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": text, "link": {"url": href}},
                            }
                        ],
                    },
                }
                blocks.append(block)
                continue

        # 引用処理
        if line.startswith(">"):
            content = line[1:].strip()
            blocks.append(
                {
                    "object": "block",
                    "type": "quote",
                    "quote": {
                        "rich_text": [{"type": "text", "text": {"content": content}}],
                    },
                }
            )
            continue

        # Markdown要素の種類をチェック
        if line.lstrip().startswith("#"):
            # '#'の数で見出しのレベルを判定
            heading_level = len(line) - len(line.lstrip("#"))
            heading_level = min(heading_level, 3)
            content = line.lstrip("#").strip()
            block = {
                "object": "block",
                "type": f"heading_{heading_level}",
                f"heading_{heading_level}": {
                    "rich_text": [{"type": "text", "text": {"content": content}}],
                },
            }
            blocks.append(block)
        elif line.lstrip().startswith("* "):
            content = line.lstrip()[2:]  # '*'とスペースを取り除いたテキスト
            block = {
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                    "rich_text": [{"type": "text", "text": {"content": content}}],
                    "children": [],
                },
            }

            if indent_level == 0:  # トップレベル
                blocks.append(block)
                current_indent_level = 0
                list_item_stack[0] = [block]  # スタックをリセット
            elif indent_level > current_indent_level:  # より深いインデント
                list_item_stack[indent_level].append(block)
                list_item_stack[indent_level - 1][-1]["bulleted_list_item"][
                    "children"
                ].append(block)
                current_indent_level = indent_level
            elif indent_level == current_indent_level:  # 同じインデントレベル
                list_item_stack[indent_level].append(block)
                list_item_stack[indent_level - 1][-1]["bulleted_list_item"][
                    "children"
                ].append(block)
            else:  # インデントレベルが減少
                current_indent_level = indent_level
                list_item_stack[indent_level].append(block)
                if indent_level > 0:  # 親リストが存在する場合
                    list_item_stack[indent_level - 1][-1]["bulleted_list_item"][
                        "children"
                    ].append(block)

        # パラグラフ（普通のテキスト）の処理
        elif line.strip() != "":  # 空行を無視
            block = {
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{"type": "text", "text": {"content": line}}],
                },
            }
            blocks.append(block)
            continue
            # 他のMarkdown要素の処理を追加...

    # スタックから空の子リストを削除
    for level_blocks in list_item_stack:
        for block in level_blocks:
            if (
                "children" in block.get("bulleted_list_item", {})
                and not block["bulleted_list_item"]["children"]
            ):
                del block["bulleted_list_item"]["children"]

    return blocks


class Notion:
    def __init__(self, notion_secret=os.getenv("NOTION_SECRET")):
        # 環境変数からNotionのAPIキーを取得する
        self.notion_secret = notion_secret
        # Notion APIのバージョン
        self.notion_headers = {
            "Authorization": f"Bearer {self.notion_secret}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json",
        }

    # ブロックを取得してMarkdownに変換する関数
    def retrieve_blocks(self, page_id, recursive, level=0, depth=0):
        read_url = f"https://api.notion.com/v1/blocks/{page_id}/children"
        markdown_content = ""
        while True:
            response = requests.get(read_url, headers=self.notion_headers)
            if response.status_code != 200:
                logging.error(
                    f"Failed to read blocks with status code {response.status_code}: {response.text} {read_url}"
                )
                break

            data = response.json()
            blocks = data.get("results", [])
            for block in blocks:
                markdown_content += "  " * level
                markdown_content += self.block_to_markdown(block, recursive, depth)
                if block.get("has_children", False):
                    markdown_content += self.retrieve_blocks(
                        block["id"], recursive, level + 1, depth
                    )

            # 'has_more'と'next_cursor'をチェックして全てのブロックを読み込む
            if not data.get("has_more", False):
                break
            read_url = f"{read_url}&start_cursor={data.get('next_cursor')}"

        return markdown_content

    def get_page_markdown(self, url, recursive=False, depth=0):
        if url.find("https://www.notion.so") == -1:
            return ""
        page_id = extract_notion_page_id(url)
        response = requests.get(
            f"https://api.notion.com/v1/pages/{page_id}", headers=self.notion_headers
        )
        page_info = response.json()

        if page_info.get("object") == "error":
            logging.error(page_info)
            return ""

        else:
            return self.retrieve_blocks(page_id, recursive, 0, depth + 1).strip()

    def get_page_database(self, url):
        if url.find("https://www.notion.so") == -1:
            return ""
        database_id = extract_notion_page_id(url)

        response = requests.post(
            f"https://api.notion.com/v1/databases/{database_id}/query",
            headers=self.notion_headers,
        )
        data = response.json()

        # ヘッダーの抽出
        headers = set()
        if data.get("object") == "error":
            logging.error(data)
            return ""

        for page in data["results"]:
            headers.update(page["properties"].keys())

        # ヘッダーをリストに変換し、ソート
        headers = sorted(list(headers))

        # 各レコードのデータを取得
        table_data = []

        for page in data["results"]:
            row = []
            for header in headers:
                property = page["properties"].get(header)
                if property:
                    property_type = property.get("type")
                    if property_type == "title":
                        title_list = property.get("title", [])
                        title = (
                            title_list[0].get("plain_text", "") if title_list else ""
                        )
                        url = page["url"]
                        row.append(f"[{title}]({url})")
                    elif property_type == "multi_select":
                        tags = [tag["name"] for tag in property.get("multi_select", [])]
                        row.append(",".join(tags))
                    elif property_type in ["last_edited_time", "created_time"]:
                        user_info = property.get(property.get("type", ""), "") or ""
                        row.append(user_info)
                    elif property_type in ["last_edited_by", "created_by"]:
                        user_info = property.get(property.get("type", ""), {}) or {}
                        row.append(f'user_{user_info["id"]}')
                    elif property_type == "select":
                        select_info = property.get("select", {}) or {}
                        row.append(select_info.get("name") or "")
                    elif property_type == "relation":
                        relation_info = ", ".join(
                            [
                                f"user_{rel['id']}"
                                for rel in property.get("relation", [])
                            ]
                        )
                        row.append(relation_info)
                    elif property_type == "url":
                        url_info = property.get("url", "") or ""
                        row.append(url_info)
                    elif property_type == "status":
                        status_info = property.get("status", {}).get("name", "") or ""
                        row.append(status_info)
                    elif property_type == "people":
                        people = property.get("people", [])
                        if people:
                            peoples = [f"user_{p['id']}" for p in people]
                            row.append(",".join(peoples))
                    elif property_type == "date":
                        pdate = property.get("date", {})
                        if pdate:
                            start = pdate.get("start", "")
                            end = pdate.get("end", "")
                            row.append(f"start:{start} end:{end}")
                    elif property_type == "rich_text":
                        rich_text = property.get("plain_text", "")
                        row.append(rich_text)
                    else:
                        # print(property_type, property)
                        row.append("")
                else:
                    row.append(str(property.get(property.get("type", ""), "")))

            table_data.append(row)

        # 一時ディレクトリを作成
        temp_dir = mkdtemp()
        csv_file_path = os.path.join(temp_dir, f"notion-database-{database_id}.csv")

        with open(csv_file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(headers)
            for row in table_data:
                writer.writerow(row)

        return csv_file_path

    def create_notion_page(self, database_id, page_title, properties={}):
        create_url = "https://api.notion.com/v1/pages"

        # ページのタイトルを設定
        data = {
            "parent": {"database_id": database_id},
            "properties": {
                "Name": {"title": [{"text": {"content": page_title}}]},
                **properties,
            },
            "children": [],
        }

        response = requests.post(create_url, headers=self.notion_headers, json=data)
        if response.status_code != 200:
            raise Exception(
                f"Failed to create page with status code {response.status_code}: {response.text}"
            )

        return response.json()

    def append_blocks_to_page(self, page_id, blocks):
        append_url = f"https://api.notion.com/v1/blocks/{page_id}/children"

        data = {"children": blocks}

        response = requests.patch(append_url, headers=self.notion_headers, json=data)
        if response.status_code != 200:
            message = f"Failed to append blocks with status code {response.status_code}: {response.text}"
            logging.error(f"{message}\n{data}")
            raise Exception(message)

    # text content helper function
    def get_text_content(self, rich_text, recursive, depth):
        text_content = ""
        for element in rich_text:
            text = element["plain_text"]
            if element["type"] == "text":
                # テキスト要素にリンクがある場合、Markdownリンク形式に変換
                if element["text"]["link"] is not None:
                    url = element["text"]["link"]["url"]
                    if url is not None:
                        text = f"[{text}]({url})\n"
                        if recursive and depth <= 3:
                            text += self.get_page_markdown(url, recursive, depth)
            elif element["type"] == "mention" and element["href"]:
                # メンションタイプの要素に対する処理（ページへのリンクなど）
                url = element["href"]
                text = f"[{text}]({url})\n"
                if recursive and depth <= 3:
                    text += self.get_page_markdown(url, recursive, depth)
            text_content += text
        return text_content.strip()

    # 特定のブロックをMarkdownに変換する関数
    def block_to_markdown(self, block, recursive, depth):
        block_type = block["type"]
        content = ""

        if block_type == "paragraph":
            content = (
                self.get_text_content(
                    block.get("paragraph", {}).get("rich_text", []), recursive, depth
                )
                + "\n"
            )
        elif block_type == "heading_1":
            content = f"# {self.get_text_content(block.get('heading_1', {}).get('rich_text', []), recursive, depth)}\n"
        elif block_type == "heading_2":
            content = f"## {self.get_text_content(block.get('heading_2', {}).get('rich_text', []), recursive, depth)}\n"
        elif block_type == "heading_3":
            content = f"### {self.get_text_content(block.get('heading_3', {}).get('rich_text', []), recursive, depth)}\n"
        elif block_type == "bulleted_list_item":
            content = f"* {self.get_text_content(block.get('bulleted_list_item', {}).get('rich_text', []), recursive, depth)}\n"
        elif block_type == "numbered_list_item":
            content = f"1. {self.get_text_content(block.get('numbered_list_item', {}).get('rich_text', []), recursive, depth)}\n"
        elif block_type == "quote":
            content = f"> {self.get_text_content(block.get('quote', {}).get('rich_text', []), recursive, depth)}\n"
        # コードブロックタイプの処理
        elif block_type == "code":
            code_content = self.get_text_content(
                block.get("code", {}).get("rich_text", []), recursive, depth
            )
            language = block["code"].get("language", "")
            content = f"```{language}\n{code_content}\n```\n"
        # `table`ブロックタイプの処理
        elif block_type == "table_row":
            # テーブルの行を処理
            row_cells = block["table_row"]["cells"]
            row_content = []
            for cell in row_cells:
                cell_content = self.get_text_content(cell, recursive, depth)
                row_content.append(cell_content)
            content = f"| {' | '.join(row_content)} |\n"
        # 他のブロックタイプの処理をここに追加...

        return content
