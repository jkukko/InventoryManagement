from application import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())

    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    incoming = db.Column(db.Boolean)
    amount = db.Column(db.Integer)

    def __init__(self, inventory_id, incoming, amount):
        self.inventory_id = inventory_id
        self.incoming = incoming
        self.amount = amount
