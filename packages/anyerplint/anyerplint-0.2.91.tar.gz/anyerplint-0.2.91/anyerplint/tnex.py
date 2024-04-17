"""tnex - Trivial Nested EXpressions.

Easier to read/write than s-expr's I guess

"""

import re

from anyerplint import util
from anyerplint.ast import Expression, FuncCall, SpecialToken


def tokenize(s: str) -> list[str]:
    # split to parts separated by ; ( ) "
    tokens = re.split(r"([\(\)\";])", s)
    filtered = list(filter(None, tokens))
    return _combine_tokens(filtered)


def _combine_tokens(tokens: list[str]) -> list[str]:
    result = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok == '"':
            s, moved = _parse_string(tokens[i:])
            result.append(s)
            i += moved
        else:
            stripped = tok.strip()
            if stripped:
                result.append(stripped)
            i += 1
    return result


class ParseError(Exception):
    """Exceptions raised by parser."""


def _parse_string(toks: list[str]) -> tuple[str, int]:
    assert toks[0] == '"'
    # eat up tokens to produce just one str
    result = ['"']
    escape = False
    for tok in util.skip(toks, 1):
        result.append(tok)
        if tok.endswith("\\"):
            backslashes = util.count_trailing(tok, "\\")
            escape = (backslashes % 2) != 0
        elif tok == '"' and not escape:
            value = "".join(result)
            return value, len(result)
        else:
            escape = False

    msg = "Unterminated string"
    raise ParseError(msg)


def _parse_accessor(first: str, toks: list[str]) -> tuple[str, int]:
    if toks and toks[0].startswith('"'):
        return first + toks[0], 2

    return first, 1


def emit_nested_sequence(
    parts: list[str], top_level: bool
) -> tuple[list[Expression], int]:
    res: list[Expression] = []
    add_empty_arg = True
    i = 0
    while i < len(parts):
        match parts[i:]:
            case [";", *_]:
                if top_level:
                    msg = "Invalid token ';' at top level of expression"
                    raise ParseError(msg)
                if add_empty_arg:
                    res.append(SpecialToken.EmptyArgument)
                add_empty_arg = True
                i += 1
            case [")", *_]:
                if top_level:
                    msg = "Invalid token ')' at top level of expression"
                    raise ParseError(msg)
                if add_empty_arg and res:
                    res.append(SpecialToken.EmptyArgument)
                i += 1
                break
            case [func_name, "(", *rest]:
                nested, moved = emit_nested_sequence(rest, top_level=False)
                func = FuncCall(name=func_name, args=nested)
                res.append(func)
                add_empty_arg = False
                i += moved + 1
            case [it, *rest] if it.startswith(","):
                # actually call previous output with "nesting" output
                s, moved = _parse_accessor(it, rest)
                try:
                    previous = res.pop()
                except IndexError as exc:
                    msg = f"',format' syntax called without preceding expression: '{s}'"
                    raise ParseError(msg) from exc

                # Not actually a function call
                fmt = FuncCall(s, [previous])
                add_empty_arg = False
                res.append(fmt)
                i += moved

            # special foo,"hello" accessor that accesses property of foo.
            # lexer breaks it because of " char, so reassemble it here
            case [it, *rest] if it.endswith(","):
                s, moved = _parse_accessor(it, rest)
                add_empty_arg = False
                res.append(s)
                i += moved
            case [it, *_]:
                add_empty_arg = False
                res.append(it.strip())
                i += 1

    return (res, i + 1)


def parse(s: str, *, expand_entities: bool = True) -> Expression:
    if expand_entities:
        s = expand_xml_entities(s)
    tokens = tokenize(s)
    parsed, _ = emit_nested_sequence(tokens, top_level=True)
    if not parsed:
        msg = f"Empty parse result for expression: '{s}'"
        raise ParseError(msg)

    return parsed[0]


def expand_xml_entities(xml_string: str) -> str:
    entity_pattern = re.compile(r"&([^;]+);")

    def replace_entity(match: re.Match[str]) -> str:
        entity = match.group(1)
        if entity == "lt":
            return "<"
        elif entity == "gt":
            return ">"
        elif entity == "amp":
            return "&"
        elif entity == "quot":
            return '"'
        else:
            return match.group(0)

    return entity_pattern.sub(replace_entity, xml_string)
