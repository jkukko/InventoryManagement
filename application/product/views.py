from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.product.models import Product
from application.product.forms import ProductForm


@app.route("/products", methods=["GET"])
def product_index():
    return render_template("product/list.html", products = Product.query.all())


@app.route("/product/new/")
@login_required
def product_form():
    return render_template("product/new.html", form = ProductForm())

@app.route("/product/", methods=["POST"])
@login_required
def product_create():
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("product/new.html", form = form)

    p = Product(form.name.data, form.segment.data)

    db.session().add(p)
    db.session.commit()

    return redirect(url_for("product_index"))
