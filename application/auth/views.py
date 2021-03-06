from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
  
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, CreateAccountForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                                error = "No such username or invalid password")


    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/new/")
def user_form():
    return render_template("/auth/new.html", form = CreateAccountForm())

@app.route("/auth/", methods=["POST"])
def user_create():
    form = CreateAccountForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)
    
    userExist = User.query.filter_by(username = form.username.data).first()
    if userExist:
        return render_template("auth/new.html", form = form, error = "Username is taken")

    u = User(username=form.username.data, password=form.password.data)

    db.session().add(u)
    db.session().commit()

    return redirect(url_for("index"))


@app.route("/auth/new/", methods=["GET", "POST"])
def auth_register():

    if request.method == "GET":
        return render_template("auth/new.html", form = CreateAccountForm())

    form = CreateAccountForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    oldUser = User.query.filter_by(username = form.username.data).first()

    if oldUser:
        return render_template("auth/new.html", form = form, error = "Username is taken")

    user = User(form.username.data, form.password.data)

    db.session.add(user)
    db.session.commit()

    return redirect(url_for("auth_login"))