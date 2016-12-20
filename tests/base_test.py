# -*- coding: utf-8 -*-

from unittest import TestCase
from stone.ast.astree import ASTree
from stone.ast.astleaf import ASTLeaf
from stone.token.token import Token
from stone.token.num_token import NumToken


class StoneTestBase(TestCase):

    def assertTokenEqual(self, one: Token, other: Token):
        self.assertEqual(one.__class__.__name__, other.__class__.__name__)
        self.assertEqual(one.line_number, other.line_number)
        self.assertEqual(one.text, other.text)
        if isinstance(one, NumToken):
            self.assertEqual(one.number, other.number)

    def assertASTLeafEqual(self, one: ASTree, other: ASTree):
        self.assertEqual(one.__class__.__name__, other.__class__.__name__)
        self.assertEqual(one.token.__class__.__name__, other.token.__class__.__name__)
        self.assertEqual(one.token.line_number, other.token.line_number)
        self.assertEqual(one.token.text, other.token.text)
        if isinstance(one.token, NumToken):
            self.assertEqual(one.token.number, other.token.number)
