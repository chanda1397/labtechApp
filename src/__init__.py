from flask import Flask
from flask_sqlalchemy import SQLAlchemy
<<<<<<< HEAD
from flask import Flask
=======
from config import *
>>>>>>> 03ce13ecfcf5bbccc76bd5beee48813fe04584d1

app = Flask(__name__)
app.config['SECRET_KEY'] = "password"


db = SQLAlchemy(app)


<<<<<<< HEAD
from src import views
app.config.from_object(__name__)
=======
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)
from common import DatabaseModel

database = DatabaseModel()

from flask_login import LoginManager

login_manager = LoginManager(app)
login_manager.login_view = "auth.login"

from src import views
>>>>>>> 03ce13ecfcf5bbccc76bd5beee48813fe04584d1
