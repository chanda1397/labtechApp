from flask import render_template, request
from src import app, login_manager, db
from src.auth import auth
from flask_login import login_required
from src.models.lab_tech import LabTech
from src.forms import CiscoKeyboard

app.register_blueprint(auth, url_prefix='/auth')


@login_manager.user_loader
def load_user(user_id):
    return LabTech.query.get(int(user_id))


@app.route('/')
def home():
    # db.session.add(LabTech(620000000, "Admin", "User", "admin@lab.com", "Password123", "ACTIVE", 'ADMIN', profile_photo="default.jpg"))
    # db.session.commit()
    #type: (int, str, str, str, str, str, str, str) -> None
    #(620000000, "Admin", "User", "admin@lab.com", "Password123", "ACTIVE", 'ADMIN', profile_photo="default.jpg")
    """Render website's home page."""
    return render_template('home.html')


@app.route('/cisco')
@login_required
def cisco():
    """Render website's cisco page."""
    return render_template('cisco.html')


@app.route('/profile', methods=['GET', 'POST'])
@app.route('/cisco/keyboard')
def cisco_keyboard():
    """Render website's cisco page."""
    form = CiscoKeyboard()
    if request.method == 'POST' and form.validate_on_submit():
        
        name = form.name.data
        serialNumber = form.serialNumber.data
        functional = form.functional.data
        
    return render_template('ciscoKeyboard.html',  form = form)


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


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    print(error)
    return "lol", 404
