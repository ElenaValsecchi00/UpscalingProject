from flask import Flask, request, jsonify
from inference import inference, get_model
from buckets import create_bucket, s3_client

app = Flask(__name__)
model = get_model()
BUCKET_NAME, _ = create_bucket(s3_client)
img = ""

@app.route('/api/upscale', methods=['POST', 'GET'])
def upscale():
    data = request.get_json() # Parse the JSON data
    if request.method == "POST":
        global img
        img = inference(data['image'], model, BUCKET_NAME)
        return jsonify({'msg': 'success', 'size': [len(img[0]), len(img)]})
    if request.method == "GET":
        return jsonify({'msg': 'success', 'size': [len(img[0]), len(img)]})


if __name__ == '__main__':
    app.run(port=5100)
    
    
