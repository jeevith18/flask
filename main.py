from flask import Flask, g, redirect, url_for, request, render_template, make_response, flash, jsonify
from flask_mail import Mail, Message
from werkzeug.utils import secure_filename
from contactform import ContactForm
from flask_sqlalchemy import SQLAlchemy
import os
import random

app = Flask(__name__)
app.secret_key="my-secret-key-flask"
app.config['MAIL_SERVER']='smtp.yopmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@yopmail.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
mail=Mail(app)
db = SQLAlchemy(app)
app.config['SIJAX_STATIC_PATH'] = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
app.config['SIJAX_JSON_URI'] = '/static/js/sijax/json2.js'

@app.route('/test_jinja/<name>')
def test_jinja_template(name):
  return render_template('test_jinja.html',name=name)

# use string in the route
@app.route('/admin')
def hello_admin():
  return 'Hello admin!'

# use string in the route
@app.route('/hello/<name>')
def hello_guest(name):
  return 'Hello %s!' % name

# use number in the route 
@app.route('/blog/<int:postID>')
def show_blog(postID):
   return 'Blog Number %d' % postID

# route using the redirect and url_for
@app.route('/user/<name>')
def hello_user(name):
  if name == 'admin':
    return redirect(url_for('hello_admin'))  # Admin goes to admin page
  else:
    return redirect(url_for('hello_guest', name=name))  # Others get personalized greeting

# method used by login method
@app.route('/success/<name>')
def success(name):
  return f'Welcome {name}!'

# post method
@app.route('/login',methods=['GET','POST'])
def login():
  if request.method == 'POST':
    user = request.form['nm']  # POST uses form data
    return redirect(url_for('success',name=user)) 
  else:
    user = request.args.get('nm')  # GET uses URL parameters
    return redirect(url_for('success',name = user))

@app.route('/student') 
def student():
  return render_template('student.html')  

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)  
    
# set a / route to check cookie
@app.route('/')
def welcome():
  username = request.cookies.get('username')
  return render_template('home.html', username=username)

@app.route('/ajax-demo')
def ajax_demo():
    return render_template('index.html')

@app.route('/setname',methods=['POST','GET'])
def set_cookie():
  if request.method == 'POST':
    username = request.form.get('username')
    if username:
      resp = make_response(redirect("/"))
      resp.set_cookie("username", username, max_age=60*60*24)
      flash(f'{username} successfully logged in...')
      return resp
  return render_template('login.html')

@app.route('/logout',methods=['POST','GET'])
def logout():
  resp = make_response(redirect('/'))
  resp.set_cookie('username', '', expires=0)
  flash("User successfully loggedout...")
  return resp

# flash message  in the page 
@app.route('/flash')
def flash_msg():
  flash('This is a custom flash message for the user!')
  flash('second flash!')
  return redirect('/')

# file uploader
@app.route('/fileupload')
def file_upload():
  return render_template('upload_file.html')

@app.route('/uploader', methods=['POST','GET'])
def uploader():
  if request.method == 'POST':
    f = request.files['file']
    f.save(secure_filename(f.filename))
    return 'file uploaded successfully!!..'
  
# mail setup  
# This is just a sample code setup how does mailing works in flask, it will not work
@app.route('/flask_mail')
def flask_mail():
  msg= Message('Test_mail',recipients="krr@yopmal.com",sender="krrish@yopmail.com")
  msg.body = 'Hello Flask message sent from Flask-Mail'
  mail.send(msg)
  return "Mail Sent"

# Create a flask specific form and use them in /form endpoint
@app.route('/contact',methods=['GET','POST'])
def flask_form():
  form = ContactForm()
  if request.method == 'POST':
    if form.validate()==False:
      return render_template('contact.html',form=form)
    else:
      return render_template('form_success.html')
  elif request.method == 'GET':
    return render_template('contact.html', form = form)
  
class student(db.Model):
  id = db.Column('student_id',db.Integer,primary_key=True)
  name = db.Column(db.String(100))
  gender = db.Column(db.String(25))

  def __init__(self,id,name,gender):
    self.id = id
    self.name = name
    self.gender = gender
    
@app.route('/show_all')
def show_all():
  return render_template('show_all.html',student_all=student.query.all)

@app.route('/new_student', methods=['GET', 'POST'])
def add_student():
  if request.method == 'POST':
    if not request.form['name'] or not request.form["gender"]:
      flash('Please enter all the fields', 'error')
    else:
      new_student = student(None, request.form['name'], request.form['gender'])
      db.session.add(new_student)
      db.session.commit()
      flash('Record was successfully added')
      return redirect(url_for('show_all'))
  return render_template('new_student.html')

# method to demostrate ajax call, this is called in index.html file using the javascript function
@app.route('/say_hello', methods=['POST'])
def say_hello():
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'yellow', 'gray', 'black']
    color = random.choice(colors)
    message = f"Hello from Flask modern AJAX! (Color: {color})"
    return jsonify(message=message, color=color)

if __name__ == '__main__':
  with app.app_context():
    db.create_all()
  app.run(debug=True)
