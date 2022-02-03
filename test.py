from main import app, db
import unittest
import json
from Models import OrderModel, ProductModel, CustomerModel


class FlaskTest(unittest.TestCase):
    def test_orders(self):
        tester = app.test_client(self)
        response = tester.get('/orders')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_customers(self):
        tester = app.test_client(self)
        response = tester.get('/customers')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_products(self):
        tester = app.test_client(self)
        response = tester.get('/products')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

    def test_order_content(self):
        tester = app.test_client(self)
        response = tester.get('/order/10248')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        expected_data = {
            "OrderID": 10248,
            "CustomerID": 10248,
            "EmployeeID": 5,
            "OrderDate": "1996-07-04 00:00:00",
            "RequiredDate": "1996-08-01 00:00:00",
            "ShippedDate": "1996-07-16 00:00:00",
            "ShipVia": 3,
            "Freight": 32.38,
            "ShipName": "Vins et alcools Chevalier",
            "ShipAddress": "59 rue de l'Abbaye",
            "ShipCity": "Reims",
            "ShipRegion": "NULL",
            "ShipPostalCode": "51100",
            "ShipCountry": "France"
        }
        self.assertEqual(response.get_json(), expected_data)

    def test_product_content(self):
        tester = app.test_client(self)
        response = tester.get('/product/1')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        expected_data = {
            "ProductID": 1,
            "ProductName": "Chai",
            "SupplierID": 1,
            "CategoryID": 1,
            "QuantityPerUnit": "10 boxes x 20 bags",
            "UnitPrice": 18.0,
            "UnitsInStock": 39,
            "UnitsOnOrder": 0,
            "ReorderLevel": 10,
            "Discontinued": False
        }
        self.assertEqual(response.get_json(), expected_data)

    def test_customer_content(self):
        tester = app.test_client(self)
        response = tester.get('/customer/VINET')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        expected_data = {
            "CustomerID": "VINET",
            "CompanyName": "Vins et alcools Chevalier",
            "ContactName": "Paul Henriot",
            "ContactTitle": "Accounting Manager",
            "Address": "59 rue de l'Abbaye",
            "City": "Reims",
            "Region": "NULL",
            "PostalCode": "51100",
            "Country": "France",
            "Phone": "26.47.15.10",
            "Fax": "26.47.15.11"
        }
        self.assertEqual(response.get_json(), expected_data)

    def test_order_insert(self):
        tester = app.test_client(self)
        order_id = 11077
        data = {
            "CustomerID": 11077,
            "EmployeeID": 4,
            "OrderDate": None,
            "RequiredDate": None,
            "ShippedDate": None,
            "ShipVia": 2,
            "Freight": 38.28,
            "ShipName": "Bon app'",
            "ShipAddress": "12 rue des Bouchers",
            "ShipCity": "Marseille",
            "ShipRegion": "NULL",
            "ShipPostalCode": "13008",
            "ShipCountry": "France"
        }
        response = tester.put(
            '/order/11077', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Message": "Inserted"})
        
        # Testing order update
        data["EmployeeID"] = 3
        response = tester.put(
            '/order/11077', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Message": "Inserted"})

        with app.app_context():
            order = OrderModel.query.filter_by(OrderID=order_id).first()
        if order:
            with app.app_context():
                db.session.delete(order)
                db.session.commit()

    def test_order_delete(self):
        tester = app.test_client(self)
        # Adding data to delete.
        order_id = 11077
        data = {
            "OrderID": 11077,
            "CustomerID": 11077,
            "EmployeeID": 4,
            "OrderDate": None,
            "RequiredDate": None,
            "ShippedDate": None,
            "ShipVia": 2,
            "Freight": 38.28,
            "ShipName": "Bon app'",
            "ShipAddress": "12 rue des Bouchers",
            "ShipCity": "Marseille",
            "ShipRegion": "NULL",
            "ShipPostalCode": "13008",
            "ShipCountry": "France"
        }
        order = OrderModel(order_id, data["CustomerID"], data["EmployeeID"], data["OrderDate"],
                           data["RequiredDate"], data["ShippedDate"], data["ShipVia"], data["Freight"],
                           data["ShipName"], data["ShipAddress"], data["ShipCity"], data["ShipRegion"],
                           data["ShipPostalCode"], data["ShipCountry"])

        with app.app_context():
            db.session.add(order)
            db.session.commit()

        response = tester.delete('/order/11077')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual({"Message": "Deleted"}, response.get_json())

        # Checking for non-existing record
        response = tester.delete('/order/11090')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Message": "Order Not Found"})

    def test_customer_insert(self):
        tester = app.test_client(self)
        data = {
            "CompanyName": "Vins et alcools Chevalier",
            "ContactName": "Paul Henriot",
            "ContactTitle": "Accounting Manager",
            "Address": "59 rue de l'Abbaye",
            "City": "Reims",
            "Region": "NULL",
            "PostalCode": "51100",
            "Country": "France",
            "Phone": "26.47.15.10",
            "Fax": "26.47.15.11"
        }
        response = tester.put(
            '/customer/VARNI', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Message": "Inserted"})
        # Testing update
        data["City"] = "Chandigarh"
        response = tester.put(
            '/customer/VARNI', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Message": "Inserted"})

        with app.app_context():
            customer = CustomerModel.query.filter_by(
                CustomerID='VARNI').first()
        if customer:
            with app.app_context():
                db.session.delete(customer)
                db.session.commit()

    def test_customer_delete(self):
        tester = app.test_client(self)
        CustomerID = 'VARNI'
        data = {
            "CompanyName": "Vins et alcools Chevalier",
            "ContactName": "Paul Henriot",
            "ContactTitle": "Accounting Manager",
            "Address": "59 rue de l'Abbaye",
            "City": "Reims",
            "Region": "NULL",
            "PostalCode": "51100",
            "Country": "France",
            "Phone": "26.47.15.10",
            "Fax": "26.47.15.11"
        }
        customer = CustomerModel(CustomerID=CustomerID, CompanyName=data["CompanyName"], ContactName=data["ContactName"], ContactTitle=data["ContactTitle"],
                                 Address=data["Address"], City=data["City"], Region=data["Region"], PostalCode=data["PostalCode"],
                                 Country=data["Country"], Phone=data["Phone"], Fax=data["Fax"])

        with app.app_context():
            db.session.add(customer)
            db.session.commit()

        response = tester.delete('/customer/VARNI')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual({"Message": "Deleted"}, response.get_json())

        # Checking for non-existing record
        response = tester.delete('/customer/KAUKA')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {
                         'Message': 'Customer Not Found'})

    def test_product_insert(self):
        tester = app.test_client(self)
        ProductID = 78
        data = {
            "ProductName": "Original Frankfurter",
            "SupplierID": 12,
            "CategoryID": 2,
            "QuantityPerUnit": "12 boxes",
            "UnitPrice": 13.0,
            "UnitsInStock": 32,
            "UnitsOnOrder": 0,
            "ReorderLevel": 15,
            "Discontinued": False

        }
        response = tester.put(
            '/product/78', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Message": "Inserted"})
        
        # Testing Update code
        data["SupplierID"] = 11
        response = tester.put(
            '/product/78', data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {"Message": "Inserted"})
        
        with app.app_context():
            product = ProductModel.query.filter_by(
                ProductID=ProductID).first()
        if product:
            with app.app_context():
                db.session.delete(product)
                db.session.commit()

    def test_product_delete(self):
        tester = app.test_client(self)
        ProductID = 78
        data = {
            "ProductName": "Original Frankfurter",
            "SupplierID": 12,
            "CategoryID": 2,
            "QuantityPerUnit": "12 boxes",
            "UnitPrice": 13.0,
            "UnitsInStock": 32,
            "UnitsOnOrder": 0,
            "ReorderLevel": 15,
            "Discontinued": False
        }
        product = ProductModel(ProductID, data["ProductName"], data["SupplierID"], data["CategoryID"],
                               data["QuantityPerUnit"], data["UnitPrice"], data["UnitsInStock"], data["UnitsOnOrder"],
                               data["ReorderLevel"], data["Discontinued"])

        with app.app_context():
            db.session.add(product)
            db.session.commit()

        response = tester.delete('/product/78')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual({"Message": "Deleted"}, response.get_json())

        # Checking for non-existing record
        response = tester.delete('/product/79')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {
                         'Message': 'Product Not Found'})


if __name__ == '__main__':
    unittest.main()
