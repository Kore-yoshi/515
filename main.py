import qrcode
from pathlib import Path

# === 输入你的内容 ===
title = "欢迎来到韩冰的个人页面"
text = "这是一个我的自拍照，欢迎大家前来欣赏！"
image_url = "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg"  # 网络图或本地文件路径

# === 生成本地 HTML 页面 ===
html_content = f"""<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        body {{
            font-family: sans-serif;
            padding: 2em;
            max-width: 800px;
            margin: auto;
        }}
        img {{
            max-width: 100%;
            border-radius: 12px;
            margin-top: 1em;
        }}
    </style>
</head>
<body>
    <h1>{title}</h1>
    <p>{text}</p>
    <img src="{image_url}" alt="展示图像">
</body>
</html>
"""

# 写入 HTML 文件
output_path = Path("content.html")
output_path.write_text(html_content, encoding="utf-8")
print(f"[+] 已创建展示页面: {output_path.resolve()}")

# === 生成二维码（指向本地文件） ===
local_url = f"file://{output_path.resolve()}"  # 适用于桌面浏览器
img = qrcode.make(local_url)
img.save("qrcode.png")
print(f"[+] 已生成二维码图片: qrcode.png")
print("[✔] 扫描二维码即可在本地浏览器打开 content.html 页面")
