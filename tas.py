from app import app

# if you want to check what's the secret key is, run python tasp.py
print(app.config['SECRET_KEY'])