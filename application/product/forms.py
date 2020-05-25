from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.Length(min=5)])
    segment = StringField("Segment", [validators.Length(min=5)])

    class Meta:
        csrf = False