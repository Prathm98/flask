from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import redirect, url_for, render_template, request
from .forms import UserForm


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from .models import User


@app.route("/")
def hello():
    return render_template("index.html", title="Title Page of Hello App", user=None)

@app.route("/users/")
def display_users():
    users = User.query.all()
    return render_template('users.html', title='Users', users=users)

@app.route("/adduser/", methods=['GET', 'POST'])
def useradd():
	form = UserForm()
	if request.method == 'POST':
		user = User(fname=form.fname.data, lname=form.lname.data, email=form.email.data)
		try:
			db.session.add(user)
			db.session.commit()
		except Exception:
			db.session.rollback()
		return render_template('adduser.html', title = 'User Input Form', username=form.fname.data, form=form)
	return render_template('adduser.html', title = 'User Input Form', form = form)

@app.route("/user/<username>/")
def hello_user(username):
    return render_template('index.html', title="User Page", user=username)    

@app.route("/user/<username>/<int:age>/")
def display_age(username, age):
    return "Hello " + username +"!!!<br>You are " + str(age) + " years old."

@app.route("/home/")
def demo_redirect():
    return redirect("http://localhost:5000/")

@app.route("/greet/user/<uname>")
def greet_user(uname):
   return redirect(url_for('hello_user', username=uname))