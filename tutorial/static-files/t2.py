from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
import os

app = FastAPI()

# 静态目录
STATIC_DIR = Path("./static")
STATIC_DIR.mkdir(parents=True, exist_ok=True)

# 挂载静态目录
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


def generate_file_tree(path: Path, base_url: str = "/static") -> str:
    print(path, base_url)
    """
    path = 文件系统路径，函数用它来查找文件
    base_url = 网页访问路径，函数用它来生成 HTML 链接
    static /static
    static/aaa /static
    static/bbb /static
    """
    """递归生成目录树的HTML"""
    items = []
    for entry in sorted(path.iterdir()):
        rel_path = entry.relative_to(STATIC_DIR)
        if entry.is_dir():
            # 目录，递归展开
            sub_tree = generate_file_tree(entry, base_url)
            items.append(
                f"<li>📂 <strong>{entry.name}/</strong><ul>{sub_tree}</ul></li>"
            )
        else:
            # 文件，生成链接
            file_url = f"{base_url}/{rel_path.as_posix()}"
            items.append(f'<li>📄 <a href="{file_url}" target="_blank">{entry.name}</a></li>')
    return "".join(items)


@app.get("/list", response_class=HTMLResponse)
async def list_files():
    """展示 static 目录文件树"""
    tree_html = generate_file_tree(STATIC_DIR)
    return f"""
    <html>
    <head>
        <meta charset="utf-8">
        <title>Static Files</title>
        <style>
            body {{ font-family: Arial, sans-serif; padding: 20px; }}
            ul {{ list-style-type: none; }}
            li {{ margin: 4px 0; }}
            a {{ text-decoration: none; color: #0077cc; }}
            a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <h2>📂 Static Directory: {STATIC_DIR}</h2>
        <ul>
            {tree_html}
        </ul>
    </body>
    </html>
    """

# http://127.0.0.1:8000/list
