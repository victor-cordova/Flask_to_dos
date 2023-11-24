from flask import flash, redirect, render_template, request, session, url_for, Blueprint
from app.forms import LoginForm

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route("/login", methods=("GET", "POST"))
def login():
    login_form = LoginForm()

    if "username" in session: 
        return redirect(url_for("index"))

    if login_form.validate_on_submit():
        user_ip = request.remote_addr
        
        session["username"] = login_form.username.data
        session["password"] = login_form.password.data
        session["user_ip"] = user_ip
        

        flash("Logged successfully")

        return redirect(url_for("index"))

    context = {
        "login_form": LoginForm()
    }
    
    return render_template("login.html", **context)

@auth.route("/")
def index():
    context = {
        "login_form": LoginForm()
    }
    return render_template("login.html", **context)