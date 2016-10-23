import requests

import time
import json

from flask_sqlalchemy import SQLAlchemy
from app import app

db = SQLAlchemy(app)

class User(db.Model):
  __tablename__ = 'users'

  """The database for current users"""
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(30))
  password = db.Column(db.String(80))
  email = db.Column(db.String(80)) 
  accountNumber = db.Column(db.String(80))

  def __init__(self, name, password, email):

    print "Generating user"
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

class Item(db.Model):
  __tablename__ = 'items'

  id = db.Column(db.Integer, primary_key=True)
  owner = db.Column(db.Integer, db.ForeignKey('users.id'))
  user = db.relationship("User", back_populates="items")

  def __init__(self, data):
    print "Generating Item"
    self.data = data

# Item mapping
User.items = db.relationship("Item", back_populates="user")




