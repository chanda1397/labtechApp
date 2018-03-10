from src.models.leb_tech.lab_tech import LabTech
from src.forms.login_form import LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from flask import Blueprint, request
from flask import render_template


auth = Blueprint("auth", __name__)


@auth.route("/register", methods = ['POST', 'GET'])
def register():

    return render_template("login.html")


@auth.route("/login", methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    error = None
    if request.method == 'POST':
        pass
    return render_template("login.html", form = form, error = error)
