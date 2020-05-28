from application import db
from application.models import Base

class Inventory(Base):
    name = db.Column(db.String(144), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    orders = db.relationship("Order", backref='inventory', lazy=True)
    products = db.relationship("Product", backref='inventory', lazy=True)

    def __init__(self, name):
        self.name = name

