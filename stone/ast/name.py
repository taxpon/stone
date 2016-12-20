# -*- coding: utf-8 -*-


from stone.ast.astleaf import ASTLeaf


class Name(ASTLeaf):

    @property
    def name(self) -> int:
        return self.token.text
