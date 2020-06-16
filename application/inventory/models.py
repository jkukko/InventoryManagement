from application import db
from application.models import Base
from sqlalchemy.sql import text

import io
import base64
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

class Inventory(Base):
    name = db.Column(db.String(144), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    orders = db.relationship("Order", backref='inventory', lazy=True)
    products = db.relationship("Product", backref='inventory', lazy=True)

    def __init__(self, name):
        self.name = name


    @staticmethod
    def count_of_products_in_inventory(inventory_id):

        stmt = text("SELECT COUNT(Product.id) FROM Product"
                    " WHERE Product.inventory_id = :inv_id").params(inv_id = inventory_id)

        res = db.engine.execute(stmt)

        for row in res:
            number = row[0]
        
        return number

    @staticmethod
    def count_of_products_in_inventory_negative_difference(inventory_id):

        stmt = text("SELECT COUNT(Product.id) FROM Product"
                    " WHERE Product.difference < 0"
                    " AND Product.inventory_id = :inv_id").params(inv_id = inventory_id)

        res = db.engine.execute(stmt)

        for row in res:
            number = row[0]
        
        return number

    @staticmethod
    def products_under_safety_stock(inventory_id):

        stmt = text("SELECT Product.name, Product.current_stock, Product.difference FROM Product"
                    " LEFT JOIN Inventory ON Inventory.id = Product.inventory_id"
                    " WHERE Product.difference < 0"
                    " AND Inventory.id = :inv").params(inv = inventory_id)

        response = []
        res = db.engine.execute(stmt)

        for row in res:
            response.append({"name": row[0], "current": row[1], "difference": row[2]})
        
        return response

    @staticmethod
    def products_current_stock_zero(inventory_id):

        stmt = text("SELECT Product.name, Product.safety_stock, Product.difference FROM Product"
                    " LEFT JOIN Inventory ON Inventory.id = Product.inventory_id"
                    " WHERE Product.current_stock = 0"
                    " AND Inventory.id = :inv").params(inv = inventory_id)

        response = []
        res = db.engine.execute(stmt)

        for row in res:
            response.append({"name": row[0], "safety_stock": row[1], "difference": row[2]})
        
        return response


    @staticmethod
    def product_id_where_difference_negative(inventory_id):

        stmt = text("SELECT Product.id FROM Product"
                    " LEFT JOIN Inventory ON Inventory.id = Product.inventory_id"
                    " WHERE Product.difference < 0"
                    " AND Inventory.id = :inv").params(inv = inventory_id)

        response = []
        res = db.engine.execute(stmt)

        for row in res:
            response.append(row[0])

        return response

    @staticmethod
    def remove_inventory(inventory_id):

        stmt = text("DELETE FROM Orders"
                    " WHERE Orders.inventory_id = :inv").params(inv = inventory_id)

        db.engine.execute(stmt)

        stmt = text("DELETE FROM Product"
                    " WHERE Product.inventory_id = :inv").params(inv = inventory_id)

        db.engine.execute(stmt)

        stmt = text("DELETE FROM Inventory"
                    " WHERE Inventory.id = :inv").params(inv = inventory_id)

        db.engine.execute(stmt)


    @staticmethod
    def get_orders_by_inventory_id(inventory_id):

        stmt = text("SELECT "
                    " Orders.date_created, "
                    " Product.name, "
                    " Orders.amount, "
                    " CASE WHEN Orders.incoming == True THEN 'Incoming' WHEN Orders.incoming == False THEN 'Outgoing' END AS Incoming FROM Orders"
                    " LEFT JOIN Product ON Product.id = Orders.product_id"
                    " WHERE Orders.inventory_id = :inv").params(inv = inventory_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"date": row[0], "product": row[1], "amount": row[2], "incoming": row[3]})

        return response

    @staticmethod
    def get_total_current_stock(inventory_id):

        stmt = text("SELECT SUM(Product.current_stock) FROM Product"
                    " WHERE Product.inventory_id = :inv").params(inv = inventory_id)

        res = db.engine.execute(stmt)

        for row in res:
            number = row[0]
        
        return number

    @staticmethod
    def get_pie_chart(inventory_id):

        stmt = text("SELECT Product.name, Product.current_stock FROM Product"
                    " WHERE Product.inventory_id = :inv").params(inv = inventory_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"product": row[0], "stock": row[1]})

        df = pd.DataFrame(response)
        print(df)
        fig, axis = plt.subplots()
        axis.pie(df["stock"], labels=df["product"], autopct='%1.1f%%', shadow=True, startangle=90)
        
        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)

        pngImageB64String = "data:image/png;base64,"
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
        return pngImageB64String



        