from application import app, db
from flask import render_template, request
from application.inventory.models import Inventory

@app.route("/inventory/new/")
def inventory_form():
    return render_template("inventory/new.html")

@app.route("/inventory/", methods=["POST"])
def inventory_create():
    i = Inventory(request.form.get("name"))

    db.session().add(i)
    db.session.commit()

    return "hello world!"