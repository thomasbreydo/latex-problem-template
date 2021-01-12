"""Generate LaTeX solution template from problems.

Template defined in template.py
"""
from collections.abc import Iterator
from typing import Union

from .template import solution_template
from .parse import parse_problems_in
from .parse import parse_problems
from .types import Filename
from urllib.parse import quote as uri_encode


class SolutionTemplate:
    problem: str
    number: str
    author: str

    def __init__(self, problem: str, number: str, author: str):
        self.problem = problem
        self.number = number
        self.author = author
        self.snip_name = f"{number} {author}"
        self.snip = solution_template.substitute(
            problem=problem, number=number, author=author
        )
        self.encoded_snip: str = uri_encode(self.snip)


class SolutionTemplateGenerator:
    author: str
    problems: list[str]
    unit_number: Union[int, str]

    def __init__(self, problems: list[str], unit_number: Union[int, str], author: str):
        self.problems = problems
        self.unit_number = unit_number
        self.author = author

    @classmethod
    def fromfile(
        cls, file: Filename, *, unit_number: Union[int, str], author: str
    ) -> "SolutionTemplateGenerator":
        return cls(parse_problems_in(file), unit_number, author)

    @classmethod
    def fromstr(
        cls, hw_code: str, *, unit_number: Union[int, str], author: str
    ) -> "SolutionTemplateGenerator":
        return cls(parse_problems(hw_code), unit_number, author)

    def __iter__(self) -> Iterator[SolutionTemplate]:
        problem: str
        i: int
        for i, problem in enumerate(self.problems, start=1):
            number: str = f"{self.unit_number}.{i}"
            yield SolutionTemplate(problem, number, self.author)
