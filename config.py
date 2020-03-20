import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'put-a-decent-cipher-here'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    
    SQLALCHEMY_DATABASE_URI = os.environ.get("mysql://tas:N7PZzbbw3m4gkaGP@66.70.179.188:3306/tas") or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False