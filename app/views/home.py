from flask import Blueprint, render_template

home = Blueprint("home", __name__, template_folder="templates", static_folder="static")


@home.route("/home", methods=["GET"])
def home_page():
    return render_template("home/layout.html")
