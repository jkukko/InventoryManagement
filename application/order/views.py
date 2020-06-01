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

    form = OrderForm()

    product = Product.query.filter(Product.id.like(form.product.data)).first()
    current_stock = product.current_stock
    value = form.amount.data
    if form.incoming.data == True:
        product.current_stock = current_stock + form.amount.data
    else:
        if current_stock > form.amount.data:
            product.current_stock = current_stock - form.amount.data
        elif current_stock == 0:
            render_template("/order/new.html", form = form)
        else:
            value = value - current_stock
            product.current_stock = 0

        

    o = Order(form.incoming.data, value)
    o.inventory_id = form.inventory.data
    o.product_id = form.product.data

    db.session().add(o)
    db.session.commit()
    return redirect(url_for("order_index"))
