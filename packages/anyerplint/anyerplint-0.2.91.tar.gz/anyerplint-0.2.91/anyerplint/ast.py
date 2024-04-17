from dataclasses import dataclass
from enum import Enum, auto
from typing import Union


class SpecialToken(Enum):
    """Special tokens that can appear in the AST."""

    EmptyArgument = auto()


Expression = Union[str, "FuncCall", SpecialToken]


@dataclass
class FuncCall:
    """An AST node representing a function call."""

    name: str
    args: list[Expression]
