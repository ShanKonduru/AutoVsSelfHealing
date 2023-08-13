from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/ux', methods=['GET'])
def serve_html():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8888)  # Change the port to 8888