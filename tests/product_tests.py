import unittest
import json
from APP.API.products import start_app


class TestEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = start_app()

    def test_post_a_product_name_is_passed_space(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/products', content_type='application/json',
                                    data=json.dumps(dict(product_name=" ",
                                                        product_price=6770000
                                                        )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())
            self.assertIn('Product field can not have space', feedbackJson['Products'])
            self.assertTrue(feedback.content_type, 'application/json')

    def test_post_a_product_is_passed_empty_field(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/products', content_type = 'application/json',
                                    data=json.dumps(dict(product_name="",
                                                         product_price=1933832
                                                         )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())                                                     
            self.assertIn('Product field can not be empty', feedbackJson['Products'])

    def test_post_a_product_price_is_passed_empty_field(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/products', content_type = 'application/json',
                                    data=json.dumps(dict(product_name="shoes",
                                                         product_price=""
                                                         )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())                                                     
            self.assertIn('Product price field cant be empty', feedbackJson['Products']) 

    def test_post_a_product_price_is_passed_empty_string(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/products', content_type = 'application/json',
                                    data=json.dumps(dict(product_name="shoes",
                                                         product_price=" "
                                                         )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())                                                     
            self.assertIn('Product price field cant be passed empty string', feedbackJson['Products'])            

    def test_post_a_product_price_is_int(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/products', content_type = 'application/json',
                                    data=json.dumps(dict(product_name="Lg",
                                                         product_price="1933832"
                                                         )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())                                                     
            self.assertIn('Product price field can not be a string', feedbackJson['Products'])                                                    
    
    def test_post_a_product_name_is_string(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/products', content_type = 'application/json',
                                    data=json.dumps(dict(product_name=234,
                                                         product_price=1933832
                                                         )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())                                                     
            self.assertIn('Product name field can not be an int', feedbackJson['Products'])  

    def test_product(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/products', content_type='application/json',
                                   data=json.dumps(dict(product_name="Samsung S6",
                                                        product_price=1500000)))
            self.assertEqual(feedback.status_code, 201)
            feedbackJson = json.loads(feedback.data.decode())
            self.assertIn("a product now exists", feedbackJson["Products"])
            self.assertTrue(feedback.content_type, 'application/json')

    def test_get_products(self):
        with self.app.test_client() as client:
            feedback = client.get("/api/v1/products/",
                                  content_type="application/json")
            self.assertEqual(feedback.status_code, 200)

    def test_get_one_product(self):
        with self.app.test_client() as client:
            feedback = client.get("/api/v1/products/1",
                                  content_type="application/json")                      
            self.assertEqual(feedback.status_code, 200)

    def test_post_a_sale_quantity_is_passed_space(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/sales', content_type='application/json',
                                    data=json.dumps(dict(sales_quantity="",
                                                         sales_price = 6770000
                                                        )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())
            self.assertIn('Sale field can not have space', feedbackJson['Sales'])
            self.assertTrue(feedback.content_type, 'application/json')        


 
    def test_post_a_sale_quantity_is_passed_empty_string(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/sales', content_type='application/json',
                                    data=json.dumps(dict(sales_quantity=" ",
                                                         sales_price = 6770000
                                                        )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())
            self.assertIn('Sale field can not be passed empty string', feedbackJson['Sales'])
            self.assertTrue(feedback.content_type, 'application/json')    
                          
    def test_post_a_sale_price_is_int(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/sales', content_type = 'application/json',
                                    data=json.dumps(dict(sales_quantity="24 sets of Lg",
                                                         sales_price="1932"
                                                         )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())                                                     
            self.assertIn('sale price field can not be a string', feedbackJson['Sales']) 

    def test_post_a_sale_price_is_passed_empty_field(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/sales', content_type = 'application/json',
                                    data=json.dumps(dict(sales_quantity="shoes",
                                                         sales_price=""
                                                         )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())                                                     
            self.assertIn('Sales price field cant be empty', feedbackJson['Sales'])  

    def test_post_a_sale_price_is_passed_empty_string(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/sales', content_type = 'application/json',
                                    data=json.dumps(dict(sales_quantity="32 samsung",
                                                         sales_price=" "
                                                         )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())                                                     
            self.assertIn('Sales price field cant be passed an empty string', feedbackJson['Sales']) 

    def test_post_a_sale_quantity_is_string(self):
        with self.app.test_client() as client:
            feedback = client.post('/api/v1/sales', content_type = 'application/json',
                                    data=json.dumps(dict(sales_quantity=234,
                                                         sales_price=1933832
                                                         )))
            self.assertEqual(feedback.status_code, 400)
            feedbackJson = json.loads(feedback.data.decode())                                                     
            self.assertIn('sale quantity field can not be an int', feedbackJson['Sales'])

    def test_get_one_sale(self):
        with self.app.test_client() as client:
            feedback = client.get("/api/v1/sales/1",
                                  content_type="application/json")                      
            self.assertEqual(feedback.status_code, 200)          
        

    if __name__ == '__main__':
        unittest.main()
