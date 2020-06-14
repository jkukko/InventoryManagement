from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField

class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=5)])
    segment = StringField("Segment", [validators.Length(min=5)])
    current_stock = IntegerField("Current Stock")
    safety_stock = IntegerField("Safety Stock")

    class Meta:
        csrf = False