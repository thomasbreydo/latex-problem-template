from typing import Optional

from flask import Blueprint, render_template, request, redirect

from solution_templates import SolutionTemplateGenerator, latex_escape

templates: Blueprint = Blueprint(
    "templates", __name__, template_folder="templates", static_folder="static"
)


@templates.route("/templates", methods=["POST"])
def templates_page_post():
    hw_code: str = request.form["hwCode"]
    unit_number: str = latex_escape(request.form["unitNumber"])
    author: str = latex_escape(request.form["author"])
    template_type: str = request.form["templateType"]
    preamble: str = request.form["preamble"]
    try:
        templates_gen: SolutionTemplateGenerator = SolutionTemplateGenerator.fromstr(
            hw_code,
            unit_number=unit_number,
            author=author,
            template_type=template_type,
            preamble=preamble,
        )
    except ValueError:
        return render_template(
            "template-generator/layout.html", error="Invalid homework LaTeX code."
        )
    return render_template(
        "templates/layout.html",
        solution_templates=list(templates_gen),
    )


@templates.route("/templates", methods=["GET"])
def templates_page_get():
    return redirect("/template-generator")
