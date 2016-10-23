# for heroku
from os import environ
import sys

from sqlalchemy import *

from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask import render_template, flash, redirect, request
from flask_login import (LoginManager, login_required, 
					login_user, logout_user, current_user)

app = Flask(__name__)

WTF_CSRF_ENABLED = True
app.secret_key='u_can_do_this'

DATABASE_URL= 'postgres://esljgsxwrspthq:uBgN3fP-XaPUaGjYOQkoe8SSBA@ec2-54-225-79-158.compute-1.amazonaws.com:5432/dfl8kk7fcsu65o'

# IF it's heroku, try will work
try:
	app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
	SQLALCHEMY_DATABASE_URI = DATABASE_URL
	print "using postgres"
# Otherwise use SQLite locally
except KeyError:
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/info.db'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///db/info.db'
	print "using sqlite"
print "success connect to db"

# login manager
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)

from models import *
from forms import *
from transfer import transfer

@app.route('/index', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def index():
	# render the forms
	register_form= RegisterForm()
	login_form = LoginForm()

	if request.method=='POST':
		# registration
		if register_form.validate_on_submit():

			if len(register_form.password.data) < 10:
				flash('Password is not long enough')
				return redirect('/')

			print('register_form validated')

			# create a new user object
			user = User(register_form.name.data, 
						register_form.email.data, 
						register_form.password.data)

			existing_user = User.query.filter_by(email=login_form.email.data).first()
			if existing_user:
				flash("This email has already been registered")
				return redirect( '/' )
			# add user to db
			db.session.add(user)
			db.session.commit()

			# login this new user
			login_user(user)
			print( "logged in user" )

			return redirect('/home')

		# logging in form validation
		if login_form.validate_on_submit():

			print('Attempt login')

			#check for user in db
			user = User.query.filter_by(email=login_form.email.data).first()
			
			# if the passwords match
			if (user and login_form.password.data == user.password):
				
				# login the user
				login_user(user)

				print('logged in user: ')
				print(current_user)

				return redirect('/home')

			# user is not in our db! turn him baaaack
			elif not user:
				flash('Wrong Email/Password Combination')
				return redirect('/index')
		
		flash('All fields are required')
		return redirect('/index')

	return render_template('index.html',
							title='Hello',
							form=register_form,
							login_form=login_form,
							current_user=current_user)

@app.route('/home', methods=["GET", "POST"])
@app.route('/home/<location>')
@login_required
def home(location="Vegas"):
	items = db.session.query(Item).filter_by(location=location.lower()).all()
	all_users = db.session.query(User).all()
	return render_template( 'home.html',
							items=items,
							title="Listings",
							all_users=all_users,
							current_user=current_user)

@app.route('/buy/<itemid>/<buyerid>')
@login_required
def buy(itemid, buyerid):
	item = db.session.query(Item).filter_by(id=itemid).first()
	buyer = db.session.query(User).filter_by(id=buyerid).first()
	seller = db.session.query(User).filter_by(id=item.owner).first()
	# Transfer item from seller to buyer

	buyer.items.append(Item(item.name, item.price, item.location))
	db.session.delete(item)

	# Pay the seller
	res = transfer(buyer.name, buyer.accountNumber, 
					 seller.name, seller.accountNumber, item.price)
	if res == "200" or res == 200:
		print "Succesfully transfered money"
		flash("Item succesfully purchased")
  
	db.session.commit()
	return redirect("/home/" + item.location)

@app.route('/add', methods=["GET", "POST"])
@login_required
def addForm():
	form = AddItemForm()
	if request.method == 'POST':
		if form.validate_on_submit:
			return redirect('/add/' + form.name.data + '/' + str(form.price.data)) + '/' + str(form.location.data)
		else:
			flash('All fields are required')
			return redirect('/add')
	return render_template('add.html',
		form=form)

@app.route('/add/<name>/<price>/<location>')
@login_required
def add(name, price):
	newItem = Item(name, price=price)
	current_user.items.append(newItem)
	db.session.add(current_user)
	db.session.commit()
	flash('Item ' + name + ' succesfully added')
	return render_template('home.html')

@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
	form = ProfileForm()
	if request.method == 'POST':
		if form.validate_on_submit:
			current_user.name = form.name.data
			current_user.email = form.email.data
			current_user.accountNumber = form.accountNumber.data
			if form.password.data:
				current_user.password = form.password.data
			db.session.commit()
			flash("Succesfully updated")
			return redirect("/profile")
		else:
			flash("An error occurred with your submission")
			return redirect("/profile")
	return render_template('profile.html',
					current_user=current_user,
					form=form)

@app.route("/logout")
def logout():
  logout_user()
  flash("You are now logged out.")
  return redirect('/')
  
# deals with unauthorized page access
@login_manager.unauthorized_handler
def unauthorized():
  # do stuff
  flash("You'll need to log in or sign up to access that page")
  return redirect('/')