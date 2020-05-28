from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application import app, db
from application.order.models import Order
from application.order.forms import OrderForm

@app.route("/orders", methods=["GET"])
def order_index():
    return render_template("order/list.html", products = Order.query.all())

@app.route("/order/new/")
@login_required
def order_form():
    return render_template("order/new.html", form=OrderForm())

@app.route("/order/", methods=["POST"])
@login_required
def order_create():

    return redirect(url_for("product_index"))
