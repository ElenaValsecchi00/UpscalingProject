from flask import Flask, request, jsonify
from inference import inference, get_model
import buckets
from cv2filters import grayscale, sharpening, noise_red, display_image

app = Flask(__name__)
model = get_model()
BUCKET_NAME, _ = buckets.create_bucket(buckets.s3_client)

@app.route('/api/edit', methods=['POST'])
def edit():
    print("sto editando")
    # Get the JSON data from the request
    data = request.get_json() # Parse the JSON data
    image_path = data['image']
    filters = data['filters']
    upscale = data['upscale']

    # Load the image from the bucket
    image = buckets.load_image(BUCKET_NAME, image_path)
    print("immagine caricata")
    
    # Apply upscale if requested
    if upscale:
        img = inference(image, model)
        print("ho inferencato")

    # Apply filters if requested as ordered in list
    for filter in filters:
        if filter == 'grayscale':
            img = grayscale(image)
        elif filter == 'sharpening':
            img = sharpening(image)
        elif filter == 'noise_red':
            img = noise_red(image)
    print("Ho filtrato")

    # Save the image to the bucket
    file_name = image_path.split('/')[-1]
    buckets.upload_to_aws(img, BUCKET_NAME, file_name +"_edited")
    print("ho uploadato")
    display_image(img)
    return jsonify('edited')

if __name__ == '__main__':
    app.run(port=5100)
