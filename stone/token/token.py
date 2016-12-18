# -*- coding: utf-8 -*-

from stone.errors import StoneException
from typing import Union


class Token(object):

    def __init__(self, line_number: int) -> None:
        self._line_number = line_number

    @property
    def line_number(self) -> int:
        return self._line_number

    @property
    def number(self) -> Union[int, float]:
        raise StoneException("not number token")

    @property
    def text(self) -> str:
        return ""

    def is_identifier(self) -> bool:
        return False

    def is_number(self) -> bool:
        return False

    def is_string(self) -> bool:
        return False


EOF = Token(-1)
STRING_EOF = "\\n"