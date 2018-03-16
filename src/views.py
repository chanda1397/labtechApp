from src import app
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from forms import MyForm



@app.route('/')

def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/cisco')
def cisco():
    """Render website's cisco page."""
    return render_template('cisco.html')

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

@app.route('/faculty')
def faculty():
    """Render website's faculty page."""
    return render_template('faculty.html')

@app.route('/engineering')
def engineering():
    """Render website's engineering page."""
    return render_template('engineering.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")


