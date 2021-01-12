from latex_problem_template import __version__
from latex_problem_template import SolutionTemplateGenerator


def test_version():
    assert __version__ == "0.1.0"


def test_parse():
    gen = SolutionTemplateGenerator.fromfile(
        "test.tex", unit_number=1, author="Thomas Breydo"
    )
    template1 = next(iter(gen))
    with open("test1answer.txt") as f:
        assert f.read() == template1.snip
