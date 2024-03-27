from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from pathlib import Path


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{Path(__file__).parent / 'market.db'}"
app.config['SECRET_KEY'] = 'ff4e997f6f3374ab4be72cb0'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
