from src import app
from flask import render_template, request, redirect, url_for, flash

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

