from application import db
from application.models import Base

class Product(Base):
    name = db.Column(db.String(144), nullable=False)
    segment = db.Column(db.String(144), nullable=False)
    current_stock = db.Column(db.Integer)
    safety_stock = db.Column(db.Integer)

    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)

    def __init__(self, name, segment):
        self.name = name
        self.segment = segment
        self.current_stock = 0
        self.safety_stock = 0

