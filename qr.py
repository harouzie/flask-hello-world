import qrcode
import json
from PIL import Image

# Tạo dữ liệu JSON
data = {
    "ssid": "ten_wifi",
    "password": "mat_khau",
    "type": "WPA2"
}

# # Chuyển đổi JSON sang chuỗi
# data_json = json.dumps(data)

wifi_data = f"""WIFI:T:{data['type']};S:{data['ssid']};P:{data["password"]};;"""

# URL của video YouTube
youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# Tạo QR code
qr = qrcode.QRCode(version=1, box_size=10)
# qr.add_data(data_json)
# qr.add_data(wifi_data)
qr.add_data(youtube_url)
qr.make(fit=True)

# Lưu QR code dạng ảnh PNG
img = qr.make_image(fill_color="black", back_color="white")
img.save("wifi_qr.png")
