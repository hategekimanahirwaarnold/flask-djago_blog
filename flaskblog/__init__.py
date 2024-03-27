import os
from dotenv import load_dotenv, dotenv_values
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = '626a5cbde150acf959863ca3a0251409'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'arnold.hirw@gmail.com'
app.config['MAIL_PASSWORD'] = 'kjgx seva klbg siiy'
mail = Mail(app)

from flaskblog import routes
