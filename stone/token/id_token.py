# -*- coding: utf-8 -*-

from stone.token.token import Token


class IdToken(Token):

    def __init__(self, line_number: int, _id: str):
        super(IdToken, self).__init__(line_number)
        self._value = _id

    @property
    def text(self) -> str:
        return self._value

    def is_id(self) -> bool:
        return True
