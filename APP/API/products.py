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