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

        