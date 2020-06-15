from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField

class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=5, message='Product name should be at least 5 characters')])
    segment = StringField("Segment", [validators.Length(min=5, message='Segment should be at least 5 characters')])
    current_stock = IntegerField("Current Stock")
    safety_stock = IntegerField("Safety Stock")

    class Meta:
        csrf = False