from application import db
from sqlalchemy import Table, Column, Integer, ForeignKey, select
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import text

orderproduct = db.Table('orderproduct', 
            db.Column('order_id', db.Integer, db.ForeignKey('order.id'), nullable=False),
            db.Column('product_id', db.Integer, db.ForeignKey('product.id'), nullable=False))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())

    incoming = db.Column(db.Boolean)
    amount = db.Column(db.Integer)

    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    products = db.relationship('Product', secondary=orderproduct, backref='Order')

    def __init__(self, inventory_id, incoming, amount):
        self.inventory_id = inventory_id
        self.incoming = incoming
        self.amount = amount
