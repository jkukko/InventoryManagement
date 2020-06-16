from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.product.models import Product
from application.product.forms import ProductForm
from application.inventory.models import Inventory

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


import io
import base64

@app.route("/inventory/<inventory_id>/products", methods=["GET"])
@login_required
def product_index(inventory_id):
    i = Inventory.query.get(inventory_id)
    products = Product.query.filter_by(inventory_id = inventory_id).all()
    count_of_products = i.count_of_products_in_inventory(inventory_id)
    
    if i.get_total_current_stock(inventory_id) == 0:
        pie_chart = ""
    elif len(products) < 1:
        pie_chart = ""
    else:
        pie_chart = i.get_pie_chart(inventory_id)

    return render_template("product/list.html", products = products, inventory = i, pie_chart = pie_chart)


@app.route("/inventory/<inventory_id>/product/new/")
@login_required
def product_form(inventory_id):
    i = Inventory.query.get(inventory_id)
    return render_template("/product/new.html", form = ProductForm(), inventory = i)

@app.route("/inventory/<inventory_id>/product/", methods=["POST"])
@login_required
def product_create(inventory_id):
    form = ProductForm(request.form)

    i = Inventory.query.get(inventory_id)

    if not form.validate():
        return render_template("product/new.html", form = form, inventory = i)

    p = Product(form.name.data, form.segment.data)

    # This is just test
    p.inventory_id = inventory_id
    i = Inventory.query.get(inventory_id)

    db.session().add(p)
    db.session().commit()

    return redirect(url_for("product_index", inventory_id=inventory_id))

@app.route("/inventory/<inventory_id>/product/<product_id>")
@login_required
def product_update_form(inventory_id, product_id):
    i = Inventory.query.get(inventory_id)
    p = Product.query.get(product_id)

    return render_template("/product/update.html", inventory=i, form = ProductForm(obj = p), product=p, chart = p.create_figure(product_id))

@app.route("/product/<product_id>", methods=["POST"])
@login_required
def product_update(product_id):

    p = Product.query.get(product_id)

    form = ProductForm(request.form)

    if not form.validate():
        return render_template("/product/update.html", inventory=i, form = ProductForm(obj = p), product=p)

    p.name = form.name.data
    p.segment = form.segment.data
    p.safety_stock = form.safety_stock.data
    p.difference = p.current_stock - form.safety_stock.data

    db.session().commit()


    return redirect(url_for("product_index", inventory_id=p.inventory_id))
