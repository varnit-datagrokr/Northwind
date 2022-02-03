from flask import Flask
from flask_restful import Api
from Models import db
from Views import CustomersView, CustomerView, OrdersView, ProductsView, OrderView, ProductView, OrderHistoryView
 
app = Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/northwind.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
api = Api(app)
db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()

api.add_resource(CustomersView, '/customers')
api.add_resource(CustomerView,'/customer/<string:CustomerID>')

api.add_resource(OrderHistoryView,'/orderhistory/<string:CustomerID>')

api.add_resource(OrdersView,'/orders')
api.add_resource(OrderView,'/order/<int:OrderID>')

api.add_resource(ProductsView,'/products')
api.add_resource(ProductView,'/product/<string:ProductID>')

app.debug = True
if __name__ == '__main__':
    app.run(host='localhost', port=5000)