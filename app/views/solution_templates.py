from flask import Blueprint, render_template, request

from latex_problem_template import SolutionTemplateGenerator, latex_escape

solution_templates = Blueprint(
    "solution_template", __name__, template_folder="templates", static_folder="static"
)


@solution_templates.route("/solution-templates", methods=["POST"])
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
        "solution-templates/layout.html", solution_templates=templates_gen
    )
