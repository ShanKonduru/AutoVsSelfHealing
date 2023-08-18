from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8888"}})

@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()
    if 'num1' in data and 'num2' in data:
        result = data['num1'] + data['num2']
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing data'}), 400

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    if 'num1' in data and 'num2' in data:
        result = data['num1'] - data['num2']
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Missing data'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
