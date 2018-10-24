class AllProducts():
    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    def myproducts(self):
        productsdata = {
            'product_id':self.product_id,
            'product_name': self.product_name,
            'product_price': self.product_price
        }
        return productsdata