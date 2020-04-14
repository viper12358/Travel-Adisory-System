from app import app,db

# run the test with python tas.py
print(app.config['SECRET_KEY'])

from app.models import User

# db.create_all()

# u = User(username='China',email='China')
# u.set_password("GreatChink")

# User.query.delete()
# db.session.commit()
