from application import db
from application.models import Base
from sqlalchemy.sql import text

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



        