from flask import Flask, send_file
import io

import qrcode

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route("/qrcode", methods=['GET'])
def qr_gen():

    youtube_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    qr = qrcode.QRCode(version=1, box_size=10)
    qr.add_data(youtube_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    # image_stream = io.BytesIO(img)

    img_byte_arr = io.BytesIO()

    # Save the PIL image to the BytesIO object
    img.save(img_byte_arr, format='PNG')

    # Rewind the BytesIO object to the beginning
    img_byte_arr.seek(0)

    return send_file(img_byte_arr, mimetype='image/png')


if __name__ == '__main__':
    app.run(debug=True)