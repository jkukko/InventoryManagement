from application import db
from application.models import Base
from sqlalchemy.sql import text

inventory_users = db.Table('inventory_users',
        db.Column('user_id', db.Integer, db.ForeignKey('account.id'), nullable=False),
        db.Column('inventory_id', db.Integer, db.ForeignKey('inventory.id'), nullable=False),                   
    )

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    inventories = db.relationship("Inventory", secondary=inventory_users)
  
    def __init__(self, username, password):
        self.username = username
        self.password = password
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True


    @staticmethod
    def get_inventories_by_user(user_id):

        stmt = text("SELECT Inventory.id, Inventory.name FROM Inventory"
                    " WHERE Inventory.id IN (SELECT inventory_users.inventory_id FROM inventory_users"
                    " WHERE inventory_users.user_id = :id)").params(id = user_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response

    @staticmethod
    def get_others_than_user_inventories(user_id):

        stmt = text("SELECT Inventory.id, Inventory.name FROM Inventory"
                    " WHERE Inventory.id NOT IN (SELECT inventory_users.inventory_id FROM inventory_users"
                    " WHERE inventory_users.user_id = :id)").params(id = user_id)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            response.append({"id": row[0], "name": row[1]})

        return response

