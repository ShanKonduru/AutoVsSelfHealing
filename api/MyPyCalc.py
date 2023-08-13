from flask import Flask, request, jsonify

app = Flask(__name__)

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
    app.run(debug=True)
