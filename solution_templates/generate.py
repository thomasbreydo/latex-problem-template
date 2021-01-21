"""Generate LaTeX solution template from problems.

Template defined in template.py
"""
from collections.abc import Iterator
from typing import Union, Optional
from urllib.parse import quote as uri_encode

from .parse import parse_problems
from .parse import parse_problems_in
from .template import basic_template, induction_template, DefaultTemplate
from .types import Filename


class SolutionTemplate:
    problem: str
    number: str
    author: str
    template: DefaultTemplate
    preamble: Optional[str]
    snip_name: str
    snip: str
    encoded_snip: str
    TEMPLATE_MAPPING: dict[str, DefaultTemplate] = {
        "basic": basic_template,
        "induction": induction_template,
    }

    def __init__(
        self,
        problem: str,
        number: str,
        author: str,
        template_type: Optional[DefaultTemplate] = None,
        preamble: Optional[str] = None,
    ):
        self.template = self._get_template(template_type)
        self.problem = problem
        self.number = number
        self.author = author
        self.preamble = preamble
        self.snip_name = f"{number} {author}"
        self.snip = self.template.substitute(
            problem=problem, title=number, author=author, preamble=preamble
        )
        self.encoded_snip = uri_encode(self.snip)

    def _get_template(self, template_type: Optional[str]):
        if not template_type:
            return basic_template
        try:
            return self.TEMPLATE_MAPPING[template_type.lower()]
        except KeyError:
            raise ValueError(f"invalid template type {template_type!r}") from None


class SolutionTemplateGenerator:
    problems: list[str]
    unit_number: Union[int, str]
    author: str
    template_type: Optional[DefaultTemplate]
    preamble: Optional[str]

    def __init__(
        self,
        problems: list[str],
        unit_number: Union[int, str],
        author: str,
        template_type: Optional[str] = None,
        preamble: Optional[str] = None,
    ):
        self.problems = problems
        self.unit_number = unit_number
        self.author = author
        self.template_type = template_type
        self.preamble = preamble

    @classmethod
    def fromfile(
        cls,
        file: Filename,
        *,
        unit_number: Union[int, str],
        author: str,
        template_type: Optional[str] = None,
        preamble: Optional[str] = None,
    ) -> "SolutionTemplateGenerator":
        return cls(
            parse_problems_in(file), unit_number, author, template_type, preamble
        )

    @classmethod
    def fromstr(
        cls,
        hw_code: str,
        *,
        unit_number: Union[int, str],
        author: str,
        template_type: Optional[str] = None,
        preamble: Optional[str] = None,
    ) -> "SolutionTemplateGenerator":
        return cls(
            parse_problems(hw_code), unit_number, author, template_type, preamble
        )

    def __iter__(self) -> Iterator[SolutionTemplate]:
        problem: str
        i: int
        for i, problem in enumerate(self.problems, start=1):
            title: str = f"{self.unit_number}.{i}"
            yield SolutionTemplate(
                problem,
                title,
                self.author,
                self.template_type,
                self.preamble,
            )
