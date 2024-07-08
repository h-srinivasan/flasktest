from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Flask Math Operations!"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b
    return jsonify({"result": result})

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    result = a - b
    return jsonify({"result": result})

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b
    return jsonify({"result": result})

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return jsonify({"error": "Division by zero is not allowed"}), 400
    
    result = a / b
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
