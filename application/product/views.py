from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.product.models import Product
from application.product.forms import ProductForm
from application.inventory.models import Inventory


@app.route("/inventory/<inventory_id>/products", methods=["GET"])
@login_required
def product_index(inventory_id):
    i = Inventory.query.get(inventory_id)   
    return render_template("product/list.html", products = Product.query.filter_by(inventory_id = inventory_id).all(), inventory = i)


@app.route("/inventory/<inventory_id>/product/new/")
@login_required
def product_form(inventory_id):
    i = Inventory.query.get(inventory_id)
    return render_template("/product/new.html", form = ProductForm(), inventory = i)

@app.route("/inventory/<inventory_id>/product/", methods=["POST"])
@login_required
def product_create(inventory_id):
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("product/new.html", form = form)

    p = Product(form.name.data, form.segment.data)

    # This is just test
    p.inventory_id = inventory_id
    i = Inventory.query.get(inventory_id)

    db.session().add(p)
    db.session.commit()

    return redirect(url_for("product_index", inventory_id=inventory_id))
