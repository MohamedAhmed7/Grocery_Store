from flask import Flask, request, jsonify
import product_dao as pr
import uom_data as um

from flask_cors import CORS, cross_origin
from db_connection import  db_connect
import json
import order_dao

app = Flask(__name__)
cors = CORS(app)

@app.route('/get_products', methods = ['GET'])
def get_products():
    connection = db_connect()
    products = pr.get_all_the_products(connection)
    response = jsonify(products)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return (response)

@app.route('/get_uom', methods = ['GET'])
def get_uom():
    connection = db_connect()
    uom = um.get_uom(connection)
    response = jsonify(uom)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return (response)

@app.route('/get_all_orders', methods=['GET'])
def get_all_orders():
    connection = db_connect()
    orders = order_dao.get_all_orders(connection)

    response = jsonify(orders)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return (response)

@app.route('/insert_order', methods=['POST'])
def insert_order():
    conection = db_connect()
    request_payload = json.loads(request.form['data'])
    print(request_payload)
    customer_name = request_payload['customer_name']
    #print(customer_name)
    order = {
        'customer_name': request_payload['customer_name']
    }
    order_id = order_dao.insert_order(connection, order)
@app.route('/delete_product', methods = ['POST'])
def delete_product():
    connection = db_connect()
    id = request.form['product_id']
    returned_id = pr.delete_product(connection, id)
    response = jsonify({
        'product_id': returned_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return (response)

@app.route('/insert_product', methods=['POST'])
def insert_product():
    connection = db_connect()
    request_payload = json.loads(request.form['data'])
    print(request_payload)
    product_id = pr.insert_new_product(connection, request_payload)

    response = jsonify({
        'prodcut_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return (response)
if __name__ == "__main__":
    print("Starting python flask server for shopping app")
    app.run(port = 5000)