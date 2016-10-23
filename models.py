import requests

import time
import json

from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class User(db.Model):

  """The database for current users"""
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30), unique=True)
  password = db.Column(db.String(80))
  email = db.Column(db.String(80)) 

  def __init__(self, name, password, email):

    print( "Generating user" )
    self.email = email
    self.name = name
    self.password = password

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    return str(self.id)

  def __repr__(self):
    return '<User %r>' % self.email

