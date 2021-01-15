from flask import Blueprint, render_template, request, redirect

from solution_templates import SolutionTemplateGenerator, latex_escape

templates = Blueprint(
    "templates", __name__, template_folder="templates", static_folder="static"
)


@templates.route("/templates", methods=["POST"])
def solution_templates_page():
    hw_code = request.form["hwCode"]
    unit_number = latex_escape(request.form["unitNumber"])
    author = latex_escape(request.form["author"])
    templates_gen: SolutionTemplateGenerator = SolutionTemplateGenerator.fromstr(
        hw_code,
        unit_number=unit_number,
        author=author,
    )
    return render_template(
        "templates/layout.html",
        solution_templates=list(templates_gen),  # todo remove
    )


@templates.route("/templates", methods=["GET"])
def solution_templates_get():
    return redirect("/template-generator")
