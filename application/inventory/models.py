from application import db

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),onupdate=db.func.current_timestamp())
    name = db.Column(db.String(144), nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    orders = db.relationship("Order", backref='inventory', lazy=True)
    products = db.relationship("Product", backref='inventory', lazy=True)

    def __init__(self, name):
        self.name = name

