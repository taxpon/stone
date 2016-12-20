# -*- coding: utf-8 -*-

from stone.ast.astree import ASTree
from stone.ast.astlist import ASTList


class BinaryExpr(ASTList):

    def left(self) -> ASTree:
        return self.child(0)

    def operator(self) -> str:
        return self.child(1).token.text

    def right(self) -> ASTree:
        return self.child(2)
