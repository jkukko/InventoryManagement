from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.inventory.models import Inventory
from application.inventory.forms import InventoryForm
from application.product.models import Product
from application.auth.models import User

@app.route("/inventories", methods=["GET"])
@login_required
def inventory_index():

    user = User.query.get(current_user.id)
    list_of_inventories = user.get_inventories_by_user(current_user.id)

    return render_template("inventory/list.html", inventories = list_of_inventories)

@app.route("/inventories/all/", methods=["GET"])
@login_required
def all_inventories():

    user = User.query.get(current_user.id)
    list_of_inventories = user.get_others_than_user_inventories(current_user.id)

    return render_template("inventory/all_inventories.html", inventories = list_of_inventories)


@app.route("/inventories/<inventory_id>/request_access", methods=["POST"])
@login_required
def add_inventory(inventory_id):

    inventory = Inventory.query.get(inventory_id)
    user = User.query.get(current_user.id)

    user.inventories.append(inventory)

    db.session.commit()

    return redirect(url_for("all_inventories"))


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

    u = User.query.get(current_user.id)

    u.inventories.append(i)
    
    db.session().add(i)
    db.session.commit()

    return redirect(url_for("inventory_index"))

@app.route("/inventory/<inventory_id>/", methods=["POST"])
@login_required
def inventory_remove(inventory_id):

    i = Inventory.query.get(inventory_id)
    user = User.query.get(current_user.id)
    list_of_inventories = user.get_inventories_by_user(current_user.id)

    if i.owner_id != current_user.id:
        i.remove_user_inventory_rows(inventory_id, current_user.id)
    else:
        i.remove_inventory(inventory_id)
    
    db.session.commit()

    return redirect(url_for("inventory_index"))


@app.route("/inventory/update/<inventory_id>", methods=["GET"])
@login_required
def inventory_update_form(inventory_id):
    i = Inventory.query.get(inventory_id)

    return render_template("/inventory/update.html", form = InventoryForm(obj = i), inventory=i)

@app.route("/inventory/update/<inventory_id>/", methods=["POST"])
@login_required
def inventory_update(inventory_id):

    i = Inventory.query.get(inventory_id)

    form = InventoryForm(request.form)

    if not form.validate():
        return render_template("/inventory/update.html", form = form, inventory=i)

    i.name = form.name.data
    
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
