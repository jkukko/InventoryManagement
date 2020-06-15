from application import db
from application.models import Base
from sqlalchemy.sql import text

class Product(Base):
    name = db.Column(db.String(144), nullable=False)
    segment = db.Column(db.String(144), nullable=False)
    current_stock = db.Column(db.Integer)
    safety_stock = db.Column(db.Integer)
    difference = db.Column(db.Integer)

    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    orders = db.relationship('Order', backref='product', lazy=True)

    def __init__(self, name, segment):
        self.name = name
        self.segment = segment
        self.current_stock = 0
        self.safety_stock = 0
        self.difference = 0
        
    def get_current_stock(self, id):
        return self.current_stock


