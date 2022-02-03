from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CustomerModel(db.Model):
    __tablename__ = 'Customers'
    CustomerID = db.Column(db.String(5), primary_key=True)
    CompanyName = db.Column(db.String(40))
    ContactName = db.Column(db.String(30))
    ContactTitle = db.Column(db.String(30))
    Address = db.Column(db.String(60))
    City = db.Column(db.String(15))
    Region = db.Column(db.String(15))
    PostalCode = db.Column(db.String(10))
    Country = db.Column(db.String(15))
    Phone = db.Column(db.String(24))
    Fax = db.Column(db.String(24))

    def __init__(self, CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax) -> None:
        self.CustomerID = CustomerID
        self.CompanyName = CompanyName
        self.ContactName = ContactName
        self.ContactTitle = ContactTitle
        self.Address = Address
        self.City = City
        self.Region = Region
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone
        self.Fax = Fax

    def json(self) -> dict:
        return {
        "CustomerID": self.CustomerID,
        "CompanyName": self.CompanyName,
        "ContactName": self.ContactName,
        "ContactTitle": self.ContactTitle,
        "Address": self.Address,
        "City": self.City,
        "Region": self.Region,
        "PostalCode": self.PostalCode,
        "Country": self.Country,
        "Phone": self.Phone,
        "Fax": self.Fax
        }

class ProductModel(db.Model):
    __tablename__ = 'Products'
    ProductID = db.Column(db.Integer, primary_key = True)
    ProductName = db.Column(db.String(40))
    SupplierID = db.Column(db.Integer)
    CategoryID = db.Column(db.Integer)
    QuantityPerUnit = db.Column(db.String(20))
    UnitPrice = db.Column(db.Float)
    UnitsInStock = db.Column(db.Integer)
    UnitsOnOrder = db.Column(db.Integer)
    ReorderLevel = db.Column(db.Integer)
    Discontinued = db.Column(db.Boolean)

    def __init__(self,ProductID,ProductName,SupplierID,CategoryID,QuantityPerUnit,UnitPrice,UnitsInStock,UnitsOnOrder,ReorderLevel,Discontinued) -> None:
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.SupplierID = SupplierID
        self.CategoryID = CategoryID
        self.QuantityPerUnit = QuantityPerUnit
        self.UnitPrice = UnitPrice
        self.UnitsInStock = UnitsInStock
        self.UnitsOnOrder = UnitsOnOrder
        self.ReorderLevel = ReorderLevel
        self.Discontinued = Discontinued

    def json(self) -> dict:
        return {
        "ProductID": self.ProductID,
        "ProductName": self.ProductName,
        "SupplierID": self.SupplierID,
        "CategoryID": self.CategoryID,
        "QuantityPerUnit": self.QuantityPerUnit,
        "UnitPrice": self.UnitPrice,
        "UnitsInStock": self.UnitsInStock,
        "UnitsOnOrder": self.UnitsOnOrder,
        "ReorderLevel": self.ReorderLevel,
        "Discontinued": self.Discontinued,
        }

class OrderModel(db.Model):
    __tablename__ = "Orders"
    OrderID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.String(5))
    EmployeeID = db.Column(db.Integer)
    OrderDate = db.Column(db.DateTime)
    RequiredDate = db.Column(db.DateTime)
    ShippedDate = db.Column(db.DateTime)
    ShipVia = db.Column(db.Integer)
    Freight = db.Column(db.Float)
    ShipName = db.Column(db.String(40))
    ShipAddress = db.Column(db.String(60))
    ShipCity = db.Column(db.String(15))
    ShipRegion = db.Column(db.String(15))
    ShipPostalCode = db.Column(db.String(10))
    ShipCountry = db.Column(db.String(15))

    def __init__(self,OrderID,CustomerID,EmployeeID,OrderDate,RequiredDate,ShippedDate,ShipVia,Freight,ShipName,ShipAddress,ShipCity,ShipRegion,ShipPostalCode,ShipCountry) -> None:
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.EmployeeID = EmployeeID
        self.OrderDate = OrderDate
        self.RequiredDate = RequiredDate
        self.ShippedDate = ShippedDate
        self.ShipVia = ShipVia
        self.Freight = Freight
        self.ShipName = ShipName
        self.ShipAddress = ShipAddress
        self.ShipCity = ShipCity
        self.ShipRegion = ShipRegion
        self.ShipPostalCode = ShipPostalCode
        self.ShipCountry = ShipCountry

    def json(self) -> dict:
        return {
            "OrderID": self.OrderID,
            "CustomerID": self.OrderID,
            "EmployeeID": self.EmployeeID,
            "OrderDate": str(self.OrderDate),
            "RequiredDate": str(self.RequiredDate),
            "ShippedDate": str(self.ShippedDate),
            "ShipVia": self.ShipVia,
            "Freight": self.Freight,
            "ShipName": self.ShipName,
            "ShipAddress": self.ShipAddress,
            "ShipCity": self.ShipCity,
            "ShipRegion": self.ShipRegion,
            "ShipPostalCode": self.ShipPostalCode,
            "ShipCountry": self.ShipCountry
        }
        