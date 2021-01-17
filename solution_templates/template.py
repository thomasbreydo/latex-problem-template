"""Define the main template for templates."""

from string import Template
from typing import Optional, Any

from .types import Mapping


class DefaultTemplate(Template):
    defaults: Mapping

    def __init__(self, template: str, defaults: Optional[Mapping] = None):
        super().__init__(template)
        self.defaults = defaults or {}

    def _combine_with_defaults(
        self, mapping: Optional[Mapping] = None, /, **kws: Any
    ) -> Mapping:
        combined_mapping: Mapping = self.defaults.copy()
        if mapping:
            combined_mapping.update(mapping)
        if kws:
            combined_mapping.update(kws)
        return combined_mapping

    def substitute(self, mapping: Optional[Mapping] = None, /, **kws: Any) -> str:
        combined_mapping: Mapping = self._combine_with_defaults(mapping, **kws)
        return super().substitute(combined_mapping)

    def safe_substitute(self, mapping: Optional[Mapping] = None, /, **kws: Any) -> str:
        combined_mapping: Mapping = self._combine_with_defaults(mapping, **kws)
        return super().safe_substitute(combined_mapping)


_basic_defaults: Mapping = dict(
    date=r"\today", preamble="", post_problem="", solution=""
)
_induction_defaults: Mapping = dict(
    _basic_defaults,
    preamble=r"\newcommand{\maxN}{TK}",
    solution=r"""
\begin{itemize}
\item The base case: prove true for $n=\maxN$.
\begin{align*}
    TK.
\end{align*}
\item The inductive hypothesis: assume true for $n=k,$ for
some $k\ge\maxN$. Then,
\begin{align*}
    TK.
\end{align*}
\item The inductive step: prove true for $n=k+1$:
\end{itemize}""",
)
_base_template_str: str = r"""\documentclass[12pt]{amsart}
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
$preamble
\begin{document}
\title{$title}
\author{$author}
\date{$date}
\maketitle

\textbf{Problem:} $problem
\vspace{0.5in} $post_problem

\textbf{Solution:} $solution
\end{document}"""


basic_template = DefaultTemplate(_base_template_str, _basic_defaults)
induction_template = DefaultTemplate(_base_template_str, _induction_defaults)
