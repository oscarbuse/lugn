# views.py

from flask import render_template

from app import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/overons')
def overons():
    return render_template("overons.html")
