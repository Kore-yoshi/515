# generate_qr.py
import qrcode
from pathlib import Path

output_dir = Path("dist")
output_dir.mkdir(exist_ok=True)

img = qrcode.make("https://your-content-or-html-link")
img.save(output_dir / "qrcode.png")

# 创建一个简单 HTML 页面
(output_dir / "index.html").write_text("""
<!DOCTYPE html>
<html>
  <body>
    <h1>扫码查看内容</h1>
    <img src="qrcode.png" alt="QR Code">
  </body>
</html>
""")
