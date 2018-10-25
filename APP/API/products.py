"""my controllers holding the HTTP requests"""
from flask import Flask, jsonify, request
from .models import AllProducts, AllSales


def start_app():
    """starting  the flask instance"""
    app = Flask(__name__)

    pdtsLists = []

    @app.route("/", strict_slashes=False)
    def index():
        return jsonify({"message":"No products are available yet."})
        
    @app.route("/api/v1/products", methods=["POST"], strict_slashes=False)
    def post_a_product():
        """params: none, post a product by postman"""
        feedback = request.get_json()
        product_id = len(pdtsLists) + 1
        product_name = feedback['product_name']
        product_price = feedback['product_price']

        if product_name == " ":
            return jsonify({"Products":"Product field can not have space"}), 400
        if product_name == "":
            return jsonify({"Products":"Product field can not be empty"}), 400
        if product_price == "":
            return jsonify({"Products":"Product price field cant be empty"}), 400
        if product_price == " ":
            return jsonify({"Products":"Product price field cant be passed empty string"}), 400
        if not isinstance(product_price, int):
            return jsonify({"Products":"Product price field can not be a string"}), 400
        if not isinstance(product_name, str):
            return jsonify({"Products":"Product name field can not be an int"}), 400

        pdtsLists.append(AllProducts(product_id, product_name, product_price))
        return jsonify({"Products": "a product now exists"}), 201


    @app.route("/api/v1/products", methods=["GET"], strict_slashes=False)
    def get_all_prducts():
        getback = []
        for pdtsList in pdtsLists:
            getback.append(pdtsList.myproducts())
        return jsonify(getback)

    @app.route("/api/v1/products/<int:product_id>", methods=["GET"], strict_slashes=False)
    def get_single_product(product_id):
        """params: product id
           for getting a product by id
        """
        single = []
        for pdtsList in pdtsLists:
            if pdtsList.product_id == product_id:
                req_dict = (pdtsList.myproducts_id())
                single.append(req_dict)
            if not single:
                return jsonify({"Products": "product does not exist"})
        else:
            return jsonify(single), 200

    salesLists = []

    @app.route("/api/v1/sales", methods=["POST"], strict_slashes=False)
    def post_a_sale():
        """for posting a sale, id auto increments"""
        dad = request.get_json()
        sales_id = len(salesLists) + 1
        sales_quantity = dad['sales_quantity']
        sales_price = dad['sales_price']


        if sales_quantity == "":
            return jsonify({"Sales":"Sale field can not have space"}), 400
        if sales_quantity == " ":
            return jsonify({"Sales":"Sale field can not be passed empty string"}), 400
        if sales_price == "":
            return jsonify({"Sales":"Sales price field cant be empty"}), 400
        if sales_price == " ":
            return jsonify({"Sales":"Sales price field cant be passed an empty string"}), 400
        if not isinstance(sales_price, int):
            return jsonify({"Sales":"sale price field can not be a string"}), 400
        if not isinstance(sales_quantity, str):
            return jsonify({"Sales":"sale quantity field can not be an int"}), 400
        salesLists.append(AllSales(sales_id, sales_quantity, sales_price))
        return jsonify({"Sales": "a sale now exists"}), 201

    @app.route("/api/v1/sales", methods=["GET"], strict_slashes=False)
    def get_all_sales():
        """get all sales"""
        getin = []
        for salesList in salesLists:
            getin.append(salesList.mysales())
        return jsonify(getin)

    @app.route("/api/v1/sales/<int:sales_id>", methods=['GET'], strict_slashes=False)
    def get_single_sale(sales_id):
        """params: None
           routes for getting a single sale
        """
        response = []
        for saleList in salesLists:
            if saleList.sales_id == sales_id:
                req_dict = (saleList.mysales())
                response.append(req_dict)
        if not response:
            return jsonify({'Sales': 'sales not found'}), 200
        else:
            return jsonify(response), 200

    return app
