from flask import render_template, request, redirect, url_for
from trustdatabase import app, db
from trustdatabase.models import Region, Trust

@app.route("/")
def home():
    trusts = list(Trust.query.order_by(Trust.trust_reg_num).all())
    regions = list(Region.query.order_by(Region.id).all())
    return render_template("home.html", trusts=trusts, regions=regions)


@app.route("/add_entry", methods=["GET", "POST"])
def add_entry():
    regions = list(Region.query.order_by(Region.region_name).all())
    if request.method == "POST":
        trust = Trust(
                    trust_reg_num=request.form.get("trust_reg_num"), 
                    trust_name=request.form.get("trust_name"),
                    region_id=request.form.get("region_id"),
                    trust_description=request.form.get("trust_description"),
                    trust_phone=request.form.get("trust_phone"),
                    trust_email=request.form.get("trust_email"),
                    trustee_names=request.form.get("trustee_names"),
                    )
        db.session.add(trust)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_entry.html", regions=regions)

@app.route("/add_region", methods=["GET", "POST"])
def add_region():
    if request.method == "POST":
        region = Region(region_name=request.form.get("region_name"))
        db.session.add(region)
        db.session.commit()
        return redirect(url_for("browse"))
    return render_template("add_region.html")

@app.route("/browse", methods=["GET"])
def browse():
    regions = list(Region.query.order_by(Region.region_name).all())
    return render_template("browse.html", regions=regions)

@app.route("/edit_region/<int:region_id>", methods=["GET", "POST"])
def edit_region(region_id):
    region = Region.query.get_or_404(region_id)
    if request.method == "POST":
        region.region_name = request.form.get("region_name")
        db.session.commit()
        return redirect(url_for("browse"))
    return render_template("edit_region.html", region=region)

@app.route("/delete_region/<int:region_id>")
def delete_region(region_id):
    region = Region.query.get_or_404(region_id)
    db.session.delete(region)
    db.session.commit()
    return redirect(url_for("browse"))

@app.route("/edit_entry/<int:trust_id>", methods=["GET", "POST"])
def edit_entry(trust_id):
    trust = Trust.query.get_or_404(trust_id)
    regions = list(Region.query.order_by(Region.region_name).all())
    if request.method == "POST":
        trust.trust_reg_num = request.form.get("trust_reg_num") 
        trust.trust_name = request.form.get("trust_name")
        trust.region_id = request.form.get("region_id")
        trust.trust_description = request.form.get("trust_description")
        trust.trust_phone = request.form.get("trust_phone")
        trust.trust_email = request.form.get("trust_email")
        trust.trustee_names = request.form.get("trustee_names")
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_entry.html", trust=trust, regions=regions)

@app.route("/delete_entry/<int:trust_id>")
def delete_entry(trust_id):
    trust = Trust.query.get_or_404(trust_id)
    db.session.delete(trust)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/region_display/<int:region_id>", methods=["GET"])
def region_display(region_id):
    trusts = list(Trust.query.order_by(Trust.trust_reg_num).all())
    region = Region.query.get_or_404(region_id)
    return render_template("region_display.html", trusts=trusts, region=region)