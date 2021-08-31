from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, validators
#from wtforms.validators import DataRequired, Length, Email
class UserForm(FlaskForm):
   fname = StringField("First Name",  [validators.DataRequired(), validators.Length(min=3, max=100)])
   lname = StringField("Last Name", [validators.DataRequired(), validators.Length(min=3, max=100)])
   email = StringField("Email", [validators.DataRequired(), validators.Email("Please provide a valid email address.")])
   submit = SubmitField("Submit")