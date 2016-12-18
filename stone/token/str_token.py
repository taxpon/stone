# -*- coding: utf-8 -*-

from stone.token.token import Token


class StrToken(Token):

    def __init__(self, line_number: int, text: str):
        super(StrToken, self).__init__(line_number)
        self._value = text

    @property
    def text(self) -> str:
        return self._value

    def is_str(self) -> bool:
        return True
