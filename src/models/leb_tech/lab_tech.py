from src import db
from flask_login import UserMixin
from random import randint
from werkzeug.security import generate_password_hash, check_password_hash


class LabTech(db.Model, UserMixin):
    __tablename__ = "users_table"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    status = db.Column(db.String(80))  # active, terminated
    profile_photo = db.Column(db.String(80))

    def __init__(self, _id, first_name, last_name, email, password, status, account_type,
                 profile_photo="default.jpg"):
        self.salt = randint()
        self.id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password + str(self.salt), method="sha256")
        self.status = status
        self.account_type = account_type
        self.profile_photo = profile_photo

    def validate_password(self, password):
        return check_password_hash(self.password, password + str(self.salt))
