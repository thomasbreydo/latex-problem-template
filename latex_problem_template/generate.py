"""Generate LaTeX solution template from problems.

Template defined in template.py
"""
from collections.abc import Iterator
from .template import solution_template
from .parse import parse_problems_in
from .parse import parse_problems
from .types import Filename


class SolutionTemplateGenerator:
    problems: list[str]
    unit_number: int

    def __init__(self, problems: list[str], unit_number: int):
        self.problems = problems
        self.unit_number = unit_number

    @classmethod
    def fromfile(cls, file: Filename, unit_number: int):
        return cls(parse_problems_in(file), unit_number)

    @classmethod
    def fromstr(cls, hw_code: str, unit_number: int):
        return cls(parse_problems(hw_code), unit_number)

    def __iter__(self) -> Iterator[str]:
        for i, problem in enumerate(self.problems, start=1):
            problem_number = f"{self.unit_number}.{i}"
            yield solution_template.substitute(number=problem_number, problem=problem)
