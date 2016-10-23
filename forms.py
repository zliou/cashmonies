from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, IntegerField, validators
from wtforms.validators import DataRequired

class RegisterForm(Form):
  name = StringField('name', validators=[DataRequired()])
  email = StringField('email', validators=[DataRequired()])
  password = PasswordField('password', validators=[validators.Length(min=6, max=35)])

class LoginForm(Form):
  email = StringField('email', validators=[DataRequired()])
  password = PasswordField('password', validators=[DataRequired()])

class AddItemForm(Form):
  name = StringField('name', validators=[DataRequired()])
  price = IntegerField('price', validators=[DataRequired()])
  location = StringField('location')

class ProfileForm(Form):
  name = StringField('name', validators=[DataRequired()])
  email = StringField('email', validators=[DataRequired()])
  password = PasswordField('password')
  accountNumber = StringField('accountNumber', validators=[DataRequired()])
