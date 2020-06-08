from flask_wtf import FlaskForm
from wtforms import validators, BooleanField, IntegerField, SelectField

class OrderForm(FlaskForm):
    
    incoming = BooleanField("Incoming/Outcoming")
    amount = IntegerField("Amount", [validators.NumberRange(min=0, max=999)])
    product = SelectField("Product", coerce=int)
    inventory = SelectField("Inventory", coerce=int)
