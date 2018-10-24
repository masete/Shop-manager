from flask import Flask, jsonify, request
from .models import AllProducts, AllSales


def start_app():
    app = Flask(__name__)

pdtsLists = []

@app.route("/api/v1/products/", methods=["GET"],strict_slashes=False)
def get_all_prducts():
    getback = []
    for pdtsList in pdtsLists:
        getback.append(pdtsList.myproducts())
    return jsonify(getback)    