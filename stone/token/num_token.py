# -*- coding: utf-8 -*-

from typing import Union
from stone.token.token import Token


class NumToken(Token):

    def __init__(self, line_number: int, value: Union[int, float]):
        super(NumToken, self).__init__(line_number)
        self._value = value

    @property
    def number(self) -> Union[int, float]:
        return self._value

    def is_number(self) -> bool:
        return True
