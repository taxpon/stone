# -*- coding: utf-8 -*-

from stone.ast.astleaf import ASTLeaf


class NumberLiteral(ASTLeaf):

    @property
    def value(self) -> int:
        return self.token.number
