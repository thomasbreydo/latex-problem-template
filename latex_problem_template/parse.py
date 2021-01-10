"""Parse the LaTeX of a homework set."""
from TexSoup import TexSoup
from .types import Filename
import re


PROBLEM_CMD = r"\problem"
ENDING_VSPACE = re.compile(r"\s*(\\vspace{.*?})+$")


def _clean_problem(problem: str) -> str:
    return re.sub(ENDING_VSPACE, "", problem.strip())


def parse_problems(hw_code: str) -> list[str]:
    soup: TexSoup = TexSoup(hw_code)
    document: str = str(soup.document)
    return [_clean_problem(problem) for problem in document.split(PROBLEM_CMD)[1:]]


def parse_problems_in(file: Filename) -> list[str]:
    with open(file) as f:
        return parse_problems(f.read())
