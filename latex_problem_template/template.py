"""Define the main template for solutions."""

from string import Template
from textwrap import dedent

r"""Usage: solution_template.substitute(number="1.34", problem="Find 1+2+\cdots+9")"""
solution_template: Template = Template(
    r"""\documentclass[12pt]{amsart}
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
\begin{document}
\title{$number}
\author{Thomas Breydo}
\date{\today}
\maketitle
\newcommand{\isit}[1]{\overset{?}{#1}}
\newcommand{\itis}[1]{\overset{\checkmark}{#1}}
\newcommand{\then}{\quad\Rightarrow\quad}


\textbf{Problem:} $problem
\vspace{0.5in}

\textbf{Solution:}
\end{document}"""
)
