from flask import render_template
from app import app
from app.forms import LoginForm

# index field
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

# login field
@app.route('/')
@app.route('/login.html')
def login():
    return render_template('login.html')
