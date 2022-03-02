from concurrent.futures import process
from crypt import methods
from urllib import response
from flask import Flask, request, jsonify, render_template
from db.firebasedb import add_one_order, get_all_orders, get_one_order

app = Flask(__name__)

@app.route('/')
def get_root():
    print('sending root')
    return render_template('index.html')

@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')

@app.route('/api')
def get_api():
    hello_dict = {'en': 'Hello', 'es': 'Hola'}
    lang = request.args.get('lang')
    return jsonify(hello_dict['en'])

@app.route('/orders', methods=["POST","GET","PUT","DELETE"])
def handle_orders():
    if request.method=="POST":
        return add_one_order(request.get_json())
    elif request.method=="GET":
        return jsonify(get_all_orders())

@app.route('/orders/<id>', methods=["GET","POST","PUT", "DELETE"])
def handle_order(id):
    if request.method=="GET":
        return jsonify(get_one_order(id))

if __name__ == '__main__':
        port =  8080
        app.run(host='0.0.0.0', port=port)