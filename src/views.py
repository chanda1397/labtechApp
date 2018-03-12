from src import app
from flask import render_template
from flask_login import login_required
from src.auth import auth


app.register_blueprint(auth, url_prefix='/auth')


@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/cisco')
@login_required
def cisco():
    """Render website's cisco page."""
    return render_template('cisco.html')


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


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    print error
    return "lol", 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
