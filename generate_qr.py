import qrcode

url = "https://Kore-yoshi.github.io/my-qrcode-site/content.html"

img = qrcode.make(url)
img.save("qrcode.png")

print("✅ 已生成公网二维码")
