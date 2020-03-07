from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# index field
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

# login field
@app.route('/')
@app.route('/login.html', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(form.username.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=form)
