from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")
  
    class Meta:
        csrf = False

class CreateAccountForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3, max=15, message='Username must be 3-15 characters')])
    password = PasswordField("Password", [validators.Length(min=3, max=15, message='Password must be 3-15 characters')])

    class Meta:
        csrf = False