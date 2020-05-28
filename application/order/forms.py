from flask_wtf import FlaskForm
from wtforms import validators, BooleanField, IntegerField, SelectField

class OrderForm(FlaskForm):
    
    incoming = BooleanField("Incoming/Outcoming")
    amount = IntegerField("Amount")
