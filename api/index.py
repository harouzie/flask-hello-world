from flask import Flask, send_file, request, jsonify
import io
import base64
import qrcode
import json

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route("/rickroll", methods=['GET'])
def rickroll():

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
    base64_data = base64.b64encode(img_byte_arr.read()).decode()

    return base64_data
    # return send_file(img_byte_arr, mimetype='image/png')


@app.route("/qrcode", methods=['GET'])
def qr_gen():

    id = request.args.get("id")

    # Validate the parameters
    if not all([id]):
        return jsonify({"error": "Missing required parameters"}), 400

    emb_string = f"{id}"

    qr = qrcode.QRCode(version=1, box_size=10, border=0)
    qr.add_data(emb_string)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    # base64_data = base64.b64encode(img_byte_arr.read()).decode()

    return send_file(img_byte_arr, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)