from flask import Flask
from flask import render_template, request, jsonify, redirect

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods = ['GET'])
@app.route('/home', methods = ['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
