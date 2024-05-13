from flask import Flask, request,jsonify
import numpy as np
import torch
from DAT.test import test_pipeline

app = Flask(__name__)
#load model
model = tf.keras.models.load_model('DAT/dat_model.py')

@app.route('/api/upscale', methods=['POST', 'GET'])
def upscale():
    return jsonify({"number": 3})

if __name__ == '__main__':
    app.run(port=5100)


'''***
from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Carica il modello di upscaling
model = tf.keras.models.load_model('modello_upscaling.h5')

def upscale_image(image):
    # Preprocessa l'immagine
    # Ad esempio, ridimensiona l'immagine in modo che sia adatta all'input del modello
    resized_image = image.resize((input_width, input_height))
    # Converti l'immagine in un array numpy
    image_array = np.array(resized_image) / 255.0  # Normalizzazione
    image_array = np.expand_dims(image_array, axis=0)  # Aggiungi una dimensione batch
    # Effettua l'upscaling dell'immagine utilizzando il modello
    upscaled_image_array = model.predict(image_array)
    # Converte l'array numpy risultante in un'immagine PIL
    upscaled_image = Image.fromarray((upscaled_image_array[0] * 255).astype(np.uint8))
    return upscaled_image

@app.route('/upscale', methods=['POST'])
def upscale():
    # Controlla se l'immagine è stata inviata correttamente
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'})
    # Legge l'immagine inviata
    image_file = request.files['image']
    image = Image.open(image_file)
    # Esegue l'upscaling dell'immagine
    upscaled_image = upscale_image(image)
    # Salva l'immagine upscalata su un buffer di memoria
    upscaled_image_buffer = io.BytesIO()
    upscaled_image.save(upscaled_image_buffer, format='JPEG')
    upscaled_image_buffer.seek(0)
    # Restituisce l'immagine upscalata al client
    return send_file(upscaled_image_buffer, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)


***'''