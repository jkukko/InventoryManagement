from application import db
from application.models import Base
from sqlalchemy.sql import text

import io
import base64
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

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

    def get_safety_stock(self,id):
        return self.safety_stock

    @staticmethod
    def orders_by_product(product_id):

        stmt = text("SELECT Orders.date_created, Orders.amount, Orders.incoming FROM Orders"
                    " WHERE Orders.product_id = :prod").params(prod = product_id)

        
        response = []
        res = db.engine.execute(stmt)

        for row in res:
            response.append({"time": row[0], "amount": row[1], "incoming": row[2]})

        return response

    @staticmethod
    def create_figure(product_id):
        p = Product.query.get(product_id)
        result_list = p.orders_by_product(product_id)
        df = pd.DataFrame(result_list)
        #df_true = df[df["incoming"]==True]
        #df_false = df[df["incoming"]==False]
        # Generate plot
        fig = Figure()
        axis = fig.add_subplot(1, 1, 1)
        axis.set_title(p.name)
        axis.set_xlabel("Inventory Level")
        axis.set_ylabel("Time")
        axis.grid()
        #axis.plot(df_true["time"], df_true["amount"], "ro-", color="green")
        #axis.plot(df_false["time"], df_false["amount"], "ro-", color="red")
        if df.size > 0:
            df["fixed_amount"] = np.where(df["incoming"] == True, df["amount"], df["amount"] * (-1))
            df["safety_stock"] = p.get_safety_stock(product_id)
            df['InventoryLevel'] = df["fixed_amount"].cumsum()
            axis.plot(df["time"], df["InventoryLevel"], "ro-", color="black")
            axis.plot(df["time"], df["safety_stock"], "ro-", color="red")        
        else:
            axis.plot(range(1), range(1), "ro-")
        
        # Convert plot to PNG image
        pngImage = io.BytesIO()
        FigureCanvas(fig).print_png(pngImage)
        
        # Encode PNG image to base64 string
        pngImageB64String = "data:image/png;base64,"
        pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')
        return pngImageB64String

