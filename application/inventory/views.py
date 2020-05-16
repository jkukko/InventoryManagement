from application import app, db
from flask import redirect, render_template, request, url_for
from application.inventory.models import Inventory

@app.route("/inventories", methods=["GET"])
def inventory_index():
    return render_template("inventory/list.html", inventories = Inventory.query.all())

@app.route("/inventory/new/")
def inventory_form():
    return render_template("inventory/new.html")

@app.route("/inventory/", methods=["POST"])
def inventory_create():
    i = Inventory(request.form.get("name"))

    db.session().add(i)
    db.session.commit()

    return redirect(url_for("inventory_index"))

@app.route("/inventory/<inventory_id>/", methods=["POST"])
def inventory_remove(inventory_id):

    i = Inventory.query.get(inventory_id)

    db.session.delete(i)
    db.session.commit()

    return redirect(url_for("inventory_index"))
