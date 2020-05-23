from flask_wtf import FlaskForm
from wtforms import StringField, validators

class InventoryForm(FlaskForm):
    name = StringField("Inventory name", [validators.Length(min=5)])

    class Meta:
        csrf = False