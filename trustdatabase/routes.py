from flask import render_template, request, redirect, url_for
from trustdatabase import app, db
from trustdatabase.models import Region, Cause, Trust

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add_entry", methods=["GET", "POST"])
def add_entry():
    if request.method == "POST":
        trust = Trust(trust_reg_num=request.form.get("trust_reg_num"), trust_name=request.form.get("trust_name"))
        db.session.add(trust)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_entry.html")

@app.route("/browse", methods=["GET"])
def browse():
    return render_template("browse.html")