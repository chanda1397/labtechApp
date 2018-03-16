<<<<<<< HEAD
from src import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import MyForm


=======
from flask import render_template
from src import app, login_manager
from src.auth import auth
from flask_login import login_required
from src.models.lab_tech import LabTech


app.register_blueprint(auth, url_prefix='/auth')


@login_manager.user_loader
def load_user(user_id):
    return LabTech.query.get(int(user_id))

>>>>>>> 03ce13ecfcf5bbccc76bd5beee48813fe04584d1

@app.route('/')

def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/cisco')
@login_required
def cisco():
    """Render website's cisco page."""
    return render_template('cisco.html')

<<<<<<< HEAD
@app.route('/profile', methods=['GET', 'POST'])
@app.route('/cisco/keyboard')
def ciscoKeyboard():
    """Render website's cisco page."""
    form = MyForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        name = form.name.data
        serialNumber = form.serialNumber.data
        functional = form.functional.data
        
    return render_template('ciscoKeyboard.html',  form = form)
=======
>>>>>>> 03ce13ecfcf5bbccc76bd5beee48813fe04584d1

@app.route('/faculty')
@login_required
def faculty():
    """Render website's faculty page."""
    return render_template('faculty.html')


@app.route('/engineering')
@login_required
def engineering():
    """Render website's engineering page."""
    return render_template('engineering.html')

<<<<<<< HEAD
@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
=======
>>>>>>> 03ce13ecfcf5bbccc76bd5beee48813fe04584d1

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    print error
    return "lol", 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
