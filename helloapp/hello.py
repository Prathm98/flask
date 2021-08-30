from flask import Flask
from flask import redirect, url_for, render_template

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html", title="Title Page of Hello App")


@app.route("/user/<username>/")
def hello_user(username):
    return '''
<html>
    <head>
       <title>User Page</title>
    </head>
    <body>
        <h1>Hello, ''' + username + '''!!!</h1>
    </body>
</html>'''

@app.route("/user/<username>/<int:age>/")
def display_age(username, age):
    return "Hello " + username +"!!!<br>You are " + str(age) + " years old."

@app.route("/home/")
def demo_redirect():
    return redirect("http://localhost:5000/")

@app.route("/greet/user/<uname>")
def greet_user(uname):
   return redirect(url_for('hello_user', username=uname))    

if __name__ == '__main__':
    app.run()