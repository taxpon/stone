# -*- coding: utf-8 -*-

from typing import List, Optional
from stone.ast.astree import ASTree


class ASTList(ASTree):

    def __init__(self, children: List[ASTree]):
        self._children = children

    def child(self, i: int):
        return self._children[i]

    def num_children(self) -> int:
        return len(self._children)

    def children(self) -> List[ASTree]:
        return self._children

    def to_string(self) -> str:
        joined = " ".join([c.to_string() for c in self.children()])
        return "({})".format(joined)

    def location(self) -> Optional[str]:
        for c in self.children():
            s = c.location()
            if s:
                return s
        return None
