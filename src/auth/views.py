from src import database
from src.forms import LoginForm
from flask import render_template
from src.validators import check_password
from flask import Blueprint, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required


auth = Blueprint("auth", __name__)


@auth.route("/register", methods=['POST', 'GET'])
@login_required
def register():
    # database.create_new_user(620000000, "Milton", "Edwards", "miltongedwards@yahoo.com", "Password123", "ACTIVE")
    # return redirect(url_for("home"))
    # return "Registered"
    return "register"


@auth.route("/login", methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    if request.args.get('error'):
        error = request.args.get('error')
    else:
        error = None
    if request.method == 'POST' and form.validate_on_submit():
        try:
            _id, password = int(form.student_id.data), form.password.data
        except ValueError:
            return redirect(url_for('auth.login', error = "Invalid User ID."))
        if not check_password(password):
            error = "Invalid Password."
        else:
            user = database.find_user_by_id(_id)
            if user:
                if user.validate_password(password):
                    login_user(user, remember=False)
                    return redirect(url_for("home"))
                else:
                    error = "Invalid Password."
            else:
                error = "User not Found."
    return render_template("login.html", form=form, error=error)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
