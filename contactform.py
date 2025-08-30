from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField,validators, ValidationError

class ContactForm(FlaskForm):
  name = StringField("Name Of Student",[validators.data_required("Please enter your name.")])
  Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
  Address = TextAreaField("Address")
   
  email = StringField("Email",[validators.data_required("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
  Age = IntegerField("age")
  language = SelectField('Languages', choices = [('cpp', 'C&plus;&plus;'), ('py', 'Python')])
  submit = SubmitField("Send")
