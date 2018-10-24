from flask import Flask, jsonify, request
from .models import AllProducts, AllSales


def start_app():
    app = Flask(__name__)

pdtsLists = []

@app.route("/api/v1/products", methods=["POST"],strict_slashes=False)
def post_a_product():
    mum = request.get_json()
    product_id = len(pdtsLists) + 1
    product_name = mum['product_name']
    product_price = mum['product_price']

    pdtsLists.append(AllProducts(product_id, product_name, product_price))
    return jsonify({"Products":"a product now exists"}), 201


@app.route("/api/v1/products/", methods=["GET"],strict_slashes=False)
def get_all_prducts():
    getback = []
    for pdtsList in pdtsLists:
        getback.append(pdtsList.myproducts())
    return jsonify(getback)  

@app.route("/api/v1/products/<int:product_id>", methods=["GET"],strict_slashes=False)
def get_single_product(product_id):
    single = []
    for pdtsList in pdtsLists:
        if pdtsList.product_id == product_id:
            req_dict = (pdtsList.myproducts_id())
            single.append(req_dict)
        if not single:
            return ({"Products":"product does not exist"})    
    else:
        return jsonify(single), 200 


salesLists = []

@app.route("/api/v1/sales", methods=["POST"],strict_slashes=False)
def post_a_sale():
    dad = request.get_json()
    sales_id = len(salesLists) + 1
    sales_quantity = dad['sales_quantity']
    sales_price    = dad['sales_price']   

    salesLists.append(AllSales(sales_id, sales_quantity, sales_price))  
    return jsonify({"Sales":"a sale now exists"}), 201

return app
