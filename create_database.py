import sqlite3
import csv
import datetime

class DB:
    def __init__(self) -> None:
        self.con = sqlite3.connect('database/northwind.db')
        self.cur = self.con.cursor()

    def __del__(self) -> None:
        try:
            self.con.close()
        except:
            pass
    
    def create_tables(self):
        # self.cur.execute('''create table employees (EmployeeID integer primary key,LastName varchar(20),FirstName text,Title text,TitleOfCourtesy text,
        # BirthDate date,HireDate date,Address text,City text,Region text,PostalCode text,Country text,HomePhone text,Extension text,Notes text,ReportsTo integer,PhotoPath text,Salary real)''')
        # self.con.commit()
        # self.cur.execute('''create table customers (CustomerID varchar(5) primary key,CompanyName varchar(40),ContactName varchar(30),ContactTitle varchar(30),Address varchar(60),
        # City varchar(15),Region varchar(15),PostalCode varchar(10),Country varchar(15),Phone varchar(24),Fax varchar(24));''')
        # self.cur.execute("drop table products;")
        # self.con.commit()
        # self.cur.execute('''create table products (ProductID integer primary key,ProductName varchar(40),SupplierID integer,CategoryID integer,QuantityPerUnit varchar(20),UnitPrice real,UnitsInStock integer,
        # UnitsOnOrder integer,ReorderLevel integer,Discontinued boolean)''')
        self.con.execute('''create table orders (OrderID integer primary key,CustomerID varchar(5),EmployeeID integer,OrderDate date,RequiredDate date,ShippedDate date,
        ShipVia integer,Freight real,ShipName varchar(40),ShipAddress varchar(60),ShipCity varchar(15),ShipRegion varchar(15),ShipPostalCode varchar(10),ShipCountry varchar(15))''')
        self.con.commit()

    def insert_data(self):
        # data = []
        # with open('csv/customers.csv','r') as rf:
        #     reader = csv.reader(rf)
        #     for i in reader:
        #         # print(len(i))
        #         data.append(tuple(i))

        # for row in data[1:]:
        #     try:
        #         self.cur.execute("insert into Customers values(?,?,?,?,?,?,?,?,?,?,?)",row)
        #         self.con.commit()
        #     except Exception as e:
        #         print(e)
        #         print(row)
        #         break
        data = []
        with open('csv/products.csv','r') as rf:
            reader = csv.reader(rf)
            for i in reader:
                # print(len(i))
                if i[9] == 0:
                    i[9] = True
                else:
                    i[9] = False
                # print(i)
                data.append(tuple(i))

        for row in data[1:]:
            # print(row)
            try:
                self.cur.execute("insert into Products values(?,?,?,?,?,?,?,?,?,?)",row)
                self.con.commit()
            except Exception as e:
                print(e)
                print(row)
                break

        data = []
        with open('csv/orders.csv','r') as rf:
            reader = csv.reader(rf)
            first = True
            for i in reader:
                if first:
                    first = False
                    continue
                for j in [3,4,5]:
                    if i[j] == 'NULL':
                        i[j] = None
                        continue
                    date = i[j].split(" ")[0].split("-")
                    i[j] = datetime.datetime(int(date[0]),int(date[1]),int(date[2]))
                data.append(tuple(i))

        for row in data:
            # print(row)
            try:
                self.cur.execute("insert into Orders values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",row)
                self.con.commit()
            except Exception as e:
                print(e)
                print(row)
                break

    def check_data(self):
        self.cur.execute('select * from orders;')
        print(self.cur.fetchone())
        

if __name__ == '__main__':
    D = DB()
    # D.create_tables()
    D.insert_data()
    # D.check_data()