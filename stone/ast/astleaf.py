# -*- coding: utf-8 -*-

from stone.ast.astree import ASTree
from stone.token.token import Token


class ASTLeaf(ASTree):

    def __init__(self, t: Token):
        self.__empty = []
        self._token = t

    def child(self, i: int):
        raise IndexError()

    def num_children(self):
        return 0

    def children(self):
        return []

    def to_string(self) -> str:
        return self._token.text

    def location(self) -> str:
        return "at line {}".format(self._token.line_number)

    @property
    def token(self):
        return self._token
