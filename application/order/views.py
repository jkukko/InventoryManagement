from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.order.models import Order
from application.product.models import Product
from application.inventory.models import Inventory
from application.order.forms import OrderForm

@app.route("/orders", methods=["GET"])
def order_index():
    return render_template("order/list.html", orders = Order.query.all())

@app.route("/order/new/")
def order_form():
    p = Product.query.all()
    names = [(i.id, i.name) for i in p]
    inv = Inventory.query.all()
    inventory_names = [(i.id, i.name) for i in inv]

    form = OrderForm()
    form.product.choices = names
    form.inventory.choices = inventory_names

    return render_template("order/new.html", form=form)

@app.route("/order/", methods=["POST"])
def order_create():
    p = Product.query.all()
    product_names = [(i.id, i.name) for i in p]
    inv = Inventory.query.all()
    inventory_names = [(i.id, i.name) for i in inv]

    form = OrderForm()
    form.product.choices = product_names
    form.inventory.choices = inventory_names

    o = Order(form.incoming.data, form.amount.data)
    o.inventory_id = 1
    o.product_id = 1

    db.session().add(o)
    db.session.commit()
    return redirect(url_for("order_index"))
