"""The models file for all data initialisation"""
class AllProducts():
    """class initialization"""
    def __init__(self, product_id, product_name, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price

    def myproducts(self):
        """format for my products data"""
        productsdata = {
            'product_id':self.product_id,
            'product_name': self.product_name,
            'product_price': self.product_price
        }
        return productsdata

    def myproducts_id(self):
        """format for my sales data"""
        productsdata = {
            'product_id':self.product_id,
            'product_name': self.product_name,
            'product_price': self.product_price
            }
        return productsdata


class AllSales():
    """class initializatin for sale"""
    def __init__(self, sales_id, sales_quantity, sales_price):
        self.sales_id = sales_id
        self.sales_quantity = sales_quantity
        self.sales_price = sales_price

    def mysales(self):
        """representation of my database"""
        salesdata = {
            'sales_id':self.sales_id,
            'sales_quantity': self.sales_quantity,
            'sales_price': self.sales_price
        }
        return salesdata
