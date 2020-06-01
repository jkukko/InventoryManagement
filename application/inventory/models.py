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
    def amount_of_products_where_current_stock_zero():
        stmt = text("SELECT COUNT(Product.id) FROM Product"
        )

        res = db.engine.execute(stmt)
        response = []
        for row in res:
            response.append(row)

        return response

