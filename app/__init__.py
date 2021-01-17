from flask import Flask, redirect

from .views.template_generator import template_generator
from .views.templates import templates

app: Flask = Flask(__name__)
app.register_blueprint(template_generator)
app.register_blueprint(templates)


@app.route("/", methods=["GET"])
def index_page():
    return redirect("/template-generator")
