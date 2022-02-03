from flask import request
from flask_restful import Resource
from Models import CustomerModel, db, ProductModel, OrderModel


class CustomersView(Resource):
    def get(self):
        customers = CustomerModel.query.all()
        return {
            "Customers": list(x.json() for x in customers)
        }


class CustomerView(Resource):
    def get(self, CustomerID: str):
        customer = CustomerModel.query.filter_by(CustomerID=CustomerID).first()
        if customer:
            return customer.json()
        return {
            "message": "Customer Not Found"
        }, 404

    def put(self, CustomerID: str):
        data = request.get_json()
        customer = CustomerModel.query.filter_by(CustomerID=CustomerID).first()
        if customer:
            customer.CompanyName = data["CompanyName"]
            customer.ContactName = data["ContactName"]
            customer.ContactTitle = data["ContactTitle"]
            customer.Address = data["Address"]
            customer.City = data["City"]
            customer.Region = data["Region"]
            customer.PostalCode = data["PostalCode"]
            customer.Country = data["Country"]
            customer.Phone = data["Phone"]
            customer.Fax = data["Fax"]
        else:
            customer = CustomerModel(CustomerID=CustomerID, CompanyName=data["CompanyName"], ContactName=data["ContactName"], ContactTitle=data["ContactTitle"],
                                     Address=data["Address"], City=data["City"], Region=data["Region"], PostalCode=data["PostalCode"],
                                     Country=data["Country"], Phone=data["Phone"], Fax=data["Fax"])

        db.session.add(customer)
        db.session.commit()
        return {"Message": "Inserted"}, 201

    def delete(self, CustomerID: str):
        customer = CustomerModel.query.filter_by(CustomerID=CustomerID).first()
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return {'Message': 'Deleted'}
        else:
            return {'Message': 'Customer Not Found'}, 404


class ProductsView(Resource):
    def get(self):
        products = ProductModel.query.all()
        return {
            "Products": list(x.json() for x in products)
        }


class ProductView(Resource):
    def get(self, ProductID: str):
        product = ProductModel.query.filter_by(ProductID=ProductID).first()
        if product:
            return product.json()
        return {
            "Message": "Product Not Found"
        }, 404

    def put(self, ProductID: str):
        data = request.get_json()
        product = ProductModel.query.filter_by(ProductID=ProductID).first()
        if product:
            product.ProductName = data["ProductName"]
            product.SupplierID = data["SupplierID"]
            product.CategoryID = data["CategoryID"]
            product.QuantityPerUnit = data["QuantityPerUnit"]
            product.UnitPrice = data["UnitPrice"]
            product.UnitsInStock = data["UnitsInStock"]
            product.UnitsOnOrder = data["UnitsOnOrder"]
            product.ReorderLevel = data["ReorderLevel"]
            product.Discontinued = data["Discontinued"]
        else:
            product = ProductModel(ProductID, data["ProductName"], data["SupplierID"], data["CategoryID"],
                                   data["QuantityPerUnit"], data["UnitPrice"], data["UnitsInStock"], data["UnitsOnOrder"],
                                   data["ReorderLevel"], data["Discontinued"])

        db.session.add(product)
        db.session.commit()
        return {"Message": "Inserted"}, 201

    def delete(self, ProductID: str):
        product = ProductModel.query.filter_by(ProductID=ProductID).first()
        if product:
            db.session.delete(product)
            db.session.commit()
            return {"Message": "Deleted"}
        else:
            return {"Message": "Product Not Found"}, 404


class OrdersView(Resource):
    def get(self):
        orders = OrderModel.query.all()
        return {
            "Orders": list(x.json() for x in orders)
        }

class OrderView(Resource):
    def get(self,OrderID:str):
        order = OrderModel.query.filter_by(OrderID=OrderID).first()
        if order:
            return order.json()
        return {
            "Message": "Order Not Found"
        }, 404

    def put(self,OrderID:str):
        data = request.get_json()
        order = OrderModel.query.filter_by(OrderID=OrderID).first()
        if order:
            order.CustomerID = data["CustomerID"]
            order.EmployeeID = data["EmployeeID"]
            order.OrderDate = data["OrderDate"]
            order.RequiredDate = data["RequiredDate"]
            order.ShippedDate = data["ShippedDate"]
            order.ShipVia = data["ShipVia"]
            order.Freight = data["Freight"]
            order.ShipName = data["ShipName"]
            order.ShipAddress = data["ShipAddress"]
            order.ShipCity = data["ShipCity"]
            order.ShipRegion = data["ShipRegion"]
            order.ShipPostalCode = data["ShipPostalCode"]
            order.ShipCountry = data["ShipCountry"]
        else:
            order = OrderModel(OrderID,data["CustomerID"],data["EmployeeID"],data["OrderDate"],
            data["RequiredDate"],data["ShippedDate"],data["ShipVia"],data["Freight"],
            data["ShipName"],data["ShipAddress"],data["ShipCity"],data["ShipRegion"],
            data["ShipPostalCode"],data["ShipCountry"])

        db.session.add(order)
        db.session.commit()

        return {"Message": "Inserted"}, 201

    def delete(self,OrderID:str):
        order = OrderModel.query.filter_by(OrderID=OrderID).first()
        if order:
            db.session.delete(order)
            db.session.commit()
            return {"Message": "Deleted"}
        else:
            return {"Message": "Order Not Found"}, 404

class OrderHistoryView(Resource):
    def get(self,CustomerID:str):
        orders = OrderModel.query.filter_by(CustomerID=CustomerID).all()
        if orders:
            return {
                "CustomerID": CustomerID,
                "Orders": list(x.json() for x in orders)
            }

        return {
            "Message": "Customer Not Found"
        }, 404