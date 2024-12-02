from flask import render_template
from trustdatabase import app, db
from trustdatabase.models import Region, Cause, Trust

@app.route("/")
def home():
    return render_template("index.html")