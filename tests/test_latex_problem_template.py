import os

from solution_templates import SolutionTemplateGenerator
from solution_templates import __version__

DIR = os.path.abspath(os.path.dirname(__file__))


def test_parse():
    gen = SolutionTemplateGenerator.fromfile(
        os.path.join(DIR, "test.tex"), unit_number=1, author="Thomas Breydo"
    )
    template1 = next(iter(gen))
    assert (
        template1.snip
        == r"""\documentclass[12pt]{amsart}
\usepackage{amssymb, latexsym}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{sidecap}
\usepackage{cancel}
\usepackage{amsthm,mathtools}
\usepackage{verbatim}
\theoremstyle{definition}
\newcommand{\isit}[1]{\overset{?}{#1}}
\newcommand{\itis}[1]{\overset{\checkmark}{#1}}
\newcommand{\then}{\quad\Rightarrow\quad}


\begin{document}
\title{1.1}
\author{Thomas Breydo}
\date{\today}
\maketitle

\textbf{Problem:} Use Gauss's method to find the sum of all of the integers between 100 and 400 which are multiples of 7.
\vspace{0.5in}

\textbf{Solution:} 
\end{document}"""
    )
