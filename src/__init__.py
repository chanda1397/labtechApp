from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import *

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY


app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = DEBUG
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)
from common import DatabaseModel

database = DatabaseModel()

from flask_login import LoginManager

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

from src import views
