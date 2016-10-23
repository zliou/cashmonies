from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, validators
from wtforms.validators import DataRequired

class RegisterForm(Form):
  name = StringField('name', validators=[DataRequired()])
  email = StringField('email', validators=[DataRequired()])
  password = PasswordField('password', validators=[validators.Length(min=6, max=35)])

class LoginForm(Form):
  email = StringField('email', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])