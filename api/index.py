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
    # Extract the required parameters
    # name = request.form.get("name")
    # id = request.form.get("id")
    # meeting_id = request.form.get("meeting_id")

    name = request.args.get("name")
    id = request.args.get("id")
    meeting_id = request.args.get("meeting_id")

    # Validate the parameters
    # if not all([name, id, meeting_id]):
    #     return jsonify({"error": "Missing required parameters"}), 400

    # Create the QR code data
    qr_data = {
        "name": name,
        # "id": id,
        "meeting_id": "mid_01",
        "command": "create_meeting"  # Replace with the actual command
    }

    # Encode the QR code data as JSON
    json_data = json.dumps(qr_data)

    qr = qrcode.QRCode(version=1, box_size=10)
    qr.add_data(json_data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    # base64_data = base64.b64encode(img_byte_arr.read()).decode()

    return send_file(img_byte_arr, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)