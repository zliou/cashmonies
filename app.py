# for heroku
from os import environ
import sys

from flask import Flask
from flask import render_template, flash, redirect, request
from flask.ext.login import (LoginManager, login_required, 
					login_user, logout_user, current_user)

app = Flask(__name__)

@app.route('/index', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def index():
	return render_template('index.html')