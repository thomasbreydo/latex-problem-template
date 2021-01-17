"""Parse the LaTeX of a homework set."""
import re
from typing import TextIO, Pattern

from TexSoup import TexSoup

from .strip_comments import strip_comments
from .types import Filename

PROBLEM_CMD: str = r"\problem"
ENDING_VSPACE: Pattern[str] = re.compile(r"\s*(\\vspace{.*?})+$")


def _clean_problem(problem: str) -> str:
    return re.sub(ENDING_VSPACE, "", problem.strip())


def parse_problems(hw_code: str) -> list[str]:
    try:
        soup: TexSoup = TexSoup(strip_comments(hw_code))
    except (TypeError, EOFError) as e:
        raise ValueError("Invalid homework LaTeX code") from e
    document: str = str(soup.document)
    return [_clean_problem(problem) for problem in document.split(PROBLEM_CMD)[1:]]


def parse_problems_in(file: Filename) -> list[str]:
    f: TextIO
    with open(file) as f:
        return parse_problems(f.read())
