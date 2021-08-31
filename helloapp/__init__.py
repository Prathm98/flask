from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import redirect, url_for, render_template


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def hello():
    return render_template("index.html", title="Title Page of Hello App", user=None)

@app.route("/users/")
def display_users():
    users = ['John', 'Rosy', 'Jack', 'Sammy', 'Lilly']
    return render_template('users.html', title='Users', users=users)


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