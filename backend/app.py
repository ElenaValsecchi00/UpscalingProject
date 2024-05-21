from flask import Flask, request, jsonify
from buckets import upload_to_aws

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    # Get the JSON data from the request
    data = request.get_json() # Parse the JSON data

    # Check if the image is in the request
    if 'image' not in data:
        return jsonify({'error': 'No image found in request'}), 400

    # Get the image data from the request
    image_bytes = data['image']

    # Save the image to the AWS S3 bucket
    image_url = upload_to_aws(image_bytes)

    # Return the image URL
    return jsonify({'image_url': image_url}), 200

@app.route('/api/edit', methods=['POST'])
def edit():
    # Get the JSON data from the request
    data = request.get_json() # Parse the JSON data

    # Check if the image is in the request
    if 'image' not in data:
        return jsonify({'error': 'No image found in request'}), 400
    elif 'filters' not in data:
        return jsonify({'error': 'No filters found in request'}), 400
    elif 'upscale' not in data:
        return jsonify({'error': 'No upscale found in request'}), 400

    # Get the image data from the request
    image_path = data['image']
    filters = data['filters']
    upscale = data['upscale']

    # Send the request to the dedicated service
    image_url = ...

    # Return the image URL
    return jsonify({'image_url': image_url}), 200

    

    
if __name__ == '__main__':
    app.run(port=5000)
