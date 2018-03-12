from src import db
from src.models import LabTech
from src.forms import LoginForm
from src.auth import Login
from flask_login import login_user, logout_user, current_user, login_required
from flask import Blueprint, request, redirect, url_for
from flask import render_template
from src import database

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=['POST', 'GET'])
def register():
    # database.create_new_user(620000000, "Milton", "Edwards", "miltongedwards@yahoo.com", "Password123", "ACTIVE")
    return "Registered"


@auth.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if request.args.get('error'):
        error = request.args.get('error')
    else:
        error = None
    if request.method == 'POST' and form.validate_on_submit():
        try:
            _id, password = int(form.student_id.data), form.password.data
        except ValueError:
            print form.student_id.data
            return redirect(url_for('auth.login', error = "Invalid User ID"))
        user = database.find_user_by_id(_id)
        if user:
            if user.validate_password(password):
                return "Logged in"
            else:
                error = "Invalid Password"
        else:
            error = "User not Found"
    return render_template("login.html", form=form, error=error)
