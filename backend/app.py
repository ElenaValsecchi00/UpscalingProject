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
    filename, _ = upload_to_aws(image_bytes)

    # Add "_result" to the filename
    result_filename = filename.replace('.', '_result.')

    # Return the resulting AWS S3 filename
    return jsonify({'result': result_filename}), 200

    
if __name__ == '__main__':
    app.run(port=5000)
