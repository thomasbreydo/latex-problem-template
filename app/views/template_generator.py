from flask import Blueprint, render_template

template_generator: Blueprint = Blueprint(
    "template-generator", __name__, template_folder="templates", static_folder="static"
)


@template_generator.route("/template-generator", methods=["GET"])
def template_generator_page():
    return render_template("template-generator/layout.html")
