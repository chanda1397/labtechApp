from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = "password"


db = SQLAlchemy(app)


from src import views
app.config.from_object(__name__)