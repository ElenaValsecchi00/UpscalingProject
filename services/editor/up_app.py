from flask import Flask, request, jsonify
from inference import inference as ups_inference
from harmo_inference import inference as harmo_inference
import buckets
from cv2filters import grayscale, sharpening, noise_red, display_image

app = Flask(__name__)
BUCKET_NAME, _ = buckets.create_bucket(buckets.s3_client)

@app.route('/api/health', methods=['GET', 'POST'])
def health():
    message = {"message": f"Service is up and running ({request.method})"}
    return jsonify(message)

@app.route('/api/edit', methods=['POST'])
def edit():
    print("sto editando")
    # Get the JSON data from the request
    data = request.get_json() # Parse the JSON data
    image_path = data['image']
    filters = data['filters']
    upscale = data['upscale']
    harmonize = data['harmonize']

    # Load the image from the bucket
    image = buckets.load_image(BUCKET_NAME, image_path)
    print("immagine caricata")
    
    # Apply upscale if requested
    if upscale:
        image = ups_inference(image)
        print("ho upscalato")

    if harmonize:
        image = harmo_inference(image)
        print("ho armonizzato")

    # Apply filters if requested as ordered in list
    for filter in filters:
        if filter == 'grayscale':
            image = grayscale(image)
        elif filter == 'sharpening':
            image = sharpening(image)
        elif filter == 'noise_red':
            image = noise_red(image)
    print("Ho filtrato")

    # Save the image to the bucket
    file_name = image_path.split('/')[-1]
    buckets.upload_to_aws(image, BUCKET_NAME, file_name +"_edited")
    print("ho uploadato")
    return jsonify('edited')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)
