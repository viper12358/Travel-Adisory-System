from app import db, login
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        digest = hashes.Hash(hashes.SHA3_256(), backend=default_backend())
        digest.update(bytes(bytearray(password, 'utf-8')))
        self.password_hash = digest.finalize()

    def check_password(self, password):
        digest = hashes.Hash(hashes.SHA3_256(), backend=default_backend())
        digest.update(bytes(bytearray(password, 'utf-8')))
        hashValue = digest.finalize()
        if hashValue == self.password_hash:
            return True
        else:
            return False

class Country(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    description = db.Column(db.String(2048))
    risks = db.Column(db.String(2048))
    environment = db.Column(db.String(2048))
    laws = db.Column(db.String(2048))
    riskLevel = db.Column(db.Integer)

    def __repr__(self):
        return '<Country {}>'.format(self.country)

    def update_details(self, data):
        self.description = data['description']
        self.risks = data['risks']
        self.environment = data['environment']
        self.laws = data['laws']
        self.riskLevel = data['riskLevel']


@login.user_loader
def load_user(id):
    return User.query.get(id)

def load_country(id):
    return Country.query.get(id)
