import werkzeug
from flask import render_template


def error404(_exception: werkzeug.exceptions.HTTPException):
    return render_template("error404/layout.html"), 404
