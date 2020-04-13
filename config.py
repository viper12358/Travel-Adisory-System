import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'put-a-decent-cipher-here'
    DISQUS_SECRET_KEY = 'Zei8rslSJzdqiT6caffCwbQkwkLru7fjpkaihXV6rqQWxWYyjAa68569zYCOJaea'
    DISQUS_PUBLIC_KEY = 'Ikja2Kv5mSSw5Iwew0w1IgCB6RKzMqYaRUIXJjgCZs1Tn9SFv2BvLFW0cA0AXrTD'


    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
