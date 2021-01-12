from latex_problem_template import strip_comments


def test_strip_comments():
    s = r"""\documentclass{article}
\begin{document}
% Easy test
just
% to
test it
%\end{document}
yk?% begone#!%
\end{document}
"""
    assert (
        strip_comments(s)
        == r"""\documentclass{article}
\begin{document}

just

test it

yk?
\end{document}
"""
    )
