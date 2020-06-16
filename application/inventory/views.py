from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.inventory.models import Inventory
from application.inventory.forms import InventoryForm
from application.product.models import Product

@app.route("/inventories", methods=["GET"])
@login_required
def inventory_index():
    return render_template("inventory/list.html", inventories = Inventory.query.filter_by(owner_id = current_user.id).all())

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
    i.owner_id = current_user.id
    
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

@app.route("/inventory/<inventory_id>/", methods=["GET"])
@login_required
def inventory(inventory_id):

    i = Inventory.query.get(inventory_id)
    
    count_of_products = i.count_of_products_in_inventory(inventory_id)
    count_of_products_negative_difference = i.count_of_products_in_inventory_negative_difference(inventory_id)
    result_list = i.products_under_safety_stock(inventory_id)

    list_of_products_current_stock_zero = i.products_current_stock_zero(inventory_id)

    list_of_products = i.product_id_where_difference_negative(inventory_id)
    list_of_charts = []

    for product_id in list_of_products:
        p = Product.query.get(product_id)
        list_of_charts.append(p.create_figure(product_id))
    

    return render_template("inventory/view.html", 
                            inventory = i, 
                            products = count_of_products, 
                            products_negative_difference = count_of_products_negative_difference, 
                            product_list = result_list,
                            products_current_stock_zero = list_of_products_current_stock_zero,
                            images = list_of_charts)
