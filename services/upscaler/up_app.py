from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/api/upscale', methods=['POST', 'GET'])
def upscale():
    return jsonify({"number": 3})

if __name__ == '__main__':
    app.run(port=5100)