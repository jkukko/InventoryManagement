from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.order.models import Order
from application.product.models import Product
from application.inventory.models import Inventory
from application.order.forms import OrderForm

@app.route("/inventory/<inventory_id>/orders", methods=["GET"])
@login_required
def order_index(inventory_id):
    i = Inventory.query.get(inventory_id)
    return render_template("order/list.html", orders = Order.query.all(), inventory = i)

@app.route("/inventory/<inventory_id>/order/new/")
@login_required
def order_form(inventory_id):
    p = Product.query.all()
    names = [(i.id, i.name) for i in p]
    i = Inventory.query.get(inventory_id)

    form = OrderForm()

    form.product.choices = names

    return render_template("order/new.html", form=form, inventory=i)

@app.route("/inventory/<inventory_id>/order/", methods=["POST"])
def order_create(inventory_id):

    form = OrderForm()

    product = Product.query.filter(Product.id.like(form.product.data)).first()
    current_stock = product.current_stock
    value = form.amount.data
    i = Inventory.query.get(inventory_id)
    
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
    o.inventory_id = inventory_id
    o.product_id = form.product.data

    db.session().add(o)
    db.session.commit()
    return redirect(url_for("order_index", inventory_id=inventory_id))
