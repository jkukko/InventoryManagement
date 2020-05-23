from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.inventory.models import Inventory
from application.inventory.forms import InventoryForm

@app.route("/inventories", methods=["GET"])
def inventory_index():
    return render_template("inventory/list.html", inventories = Inventory.query.all())

@app.route("/inventory/new/")
@login_required
def inventory_form():
    return render_template("inventory/new.html", form = InventoryForm())

@app.route("/inventory/", methods=["POST"])
@login_required
def inventory_create():
    form = InventoryForm(request.form)

    if not form.validate():
        return render_template("inventory/new.html", form = form)

    i = Inventory(form.name.data)

    db.session().add(i)
    db.session.commit()

    return redirect(url_for("inventory_index"))

@app.route("/inventory/<inventory_id>/", methods=["POST"])
@login_required
def inventory_remove(inventory_id):

    i = Inventory.query.get(inventory_id)

    db.session.delete(i)
    db.session.commit()

    return redirect(url_for("inventory_index"))
