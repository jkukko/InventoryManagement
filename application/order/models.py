from application import db
from application.models import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, select
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import text

#orderproduct = db.Table('orderproduct', 
#            db.Column('order_id', db.Integer, db.ForeignKey('orders.id'), nullable=False),
#            db.Column('product_id', db.Integer, db.ForeignKey('product.id'), nullable=False))


class Order(Base):


    __tablename__ = "orders"

    incoming = db.Column(db.Boolean)
    amount = db.Column(db.Integer)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#    products = db.relationship('Product', secondary=orderproduct, backref='Order')

    def __init__(self, incoming, amount):
        self.incoming = incoming
        self.amount = amount