from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST','GET'])
def api():
    if request.method=='POST':
        pass
    if request.method=='GET':
        return jsonify({'message': 'Hello, World!'})
    
if __name__ == '__main__':
    app.run(port=5000)
