from flask import Flask, request, jsonify
import numpy as np
import torch
from DAT.inference import inference

app = Flask(__name__)


@app.route('/api/upscale', methods=['POST', 'GET'])
def upscale():
    # TODO: Call inference function on the image
    return jsonify({"number": 3})


if __name__ == '__main__':
    app.run(port=5100)
