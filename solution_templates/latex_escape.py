import re
from typing import Pattern

EASY: Pattern[str] = re.compile(r"([&%$#_{}])")
BACKSLASHES: Pattern[str] = re.compile(r"\\")
CARETS: Pattern[str] = re.compile(r"\^")
TILDES: Pattern[str] = re.compile(r"~")
SPACES: Pattern[str] = re.compile(r"(?<![^\\]\\textbackslash)\s")


def latex_escape(string: str):
    string = string.replace("\\", r"\textbackslash ")
    string = SPACES.sub(r"\\ ", string)
    string = CARETS.sub(r"\\textasciicircum ", string)
    string = TILDES.sub(r"\\textasciitilde ", string)
    string = EASY.sub(r"\\\1", string)
    return string
