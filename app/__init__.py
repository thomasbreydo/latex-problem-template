from flask import Flask, redirect

from .views.error404 import error404
from .views.template_generator import template_generator
from .views.templates import templates

app: Flask = Flask(__name__)
app.register_blueprint(template_generator)
app.register_blueprint(templates)
app.register_error_handler(404, error404)


@app.route("/", methods=["GET"])
def index_page():
    return redirect("/template-generator")
