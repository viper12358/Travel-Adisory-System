from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

def init_db():
    User.query.delete()
    china = User(username='China', email='China@gov.com')
    china.set_password('GreatCheng')
    db.session.add(china)
    canada = User(username='Canada', email='Canada@gov.com')
    canada.set_password('HockeyMapleLeaf')
    db.session.add(canada)
    db.session.commit()

init_db()

# index field
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


# login field
@app.route('/')
@app.route('/login.html', methods=['GET','POST'])
def login():
    # basically if you are already logged in, you are automatically stay in index
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    return render_template('login.html', form=form)


@app.route('/')
@app.route("/logout", methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))
    # return render_template('logout.html')

@app.route('/')
@app.route("/management", methods=['GET','POST'])
@login_required
def management():

    # user = User.query.filter_by(username=username).first_or_404()

    return render_template('management.html')
