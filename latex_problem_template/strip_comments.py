import ply.lex as lex

tokens = (
    "PERCENT",
    "BEGINCOMMENT",
    "ENDCOMMENT",
    "BACKSLASH",
    "CHAR",
    "BEGINVERBATIM",
    "ENDVERBATIM",
    "NEWLINE",
    "ESCPCT",
)

states = (
    ("linecomment", "exclusive"),
    ("commentenv", "exclusive"),
    ("verbatim", "exclusive"),
)


def t_ANY_BACKSLASH(t):  # noqa
    r"\\\\"  # noqa
    return t


def t_PERCENT(t):  # noqa
    r"\%"  # noqa
    t.lexer.begin("linecomment")


def t_ESCPCT(t):  # noqa
    r"\\\%"  # noqa
    return t


def t_BEGINCOMMENT(t):  # noqa
    r"\\begin\s*{\s*comment\s*}"  # noqa
    t.lexer.begin("commentenv")


def t_BEGINVERBATIM(t):  # noqa
    r"\\begin\s*{\s*verbatim\s*}"  # noqa
    t.lexer.begin("verbatim")
    return t


def t_CHAR(t):  # noqa
    r"."  # noqa
    return t


def t_NEWLINE(t):  # noqa
    r"\n"  # noqa
    return t


def t_commentenv_ENDCOMMENT(t):  # noqa
    r"\\end\s*{\s*comment\s*}"  # noqa
    # Anything after \end{comment} on a line is ignored!
    t.lexer.begin("linecomment")


def t_commentenv_CHAR(t):  # noqa
    r"."  # noqa


def t_commentenv_NEWLINE(t):  # noqa
    r"\n"  # noqa


def t_verbatim_ENDVERBATIM(t):  # noqa
    r"\\end\s*{\s*verbatim\s*}"  # noqa
    t.lexer.begin("INITIAL")
    return t


def t_verbatim_CHAR(t):  # noqa
    r"."  # noqa
    return t


def t_verbatim_NEWLINE(t):  # noqa
    r"\n"  # noqa
    return t


def t_linecomment_ENDCOMMENT(t):  # noqa
    r"\n"  # noqa
    t.lexer.begin("INITIAL")
    return t


def t_linecomment_CHAR(t):  # noqa
    r"."  # noqa


def strip_comments(source):
    lexer = lex.lex(errorlog=lex.NullLogger())
    lexer.input(source)
    return "".join([tok.value for tok in lexer])
