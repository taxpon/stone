# -*- coding: utf-8 -*-

from tests.base_test import StoneTestBase
from stone.ast.astleaf import ASTLeaf
from stone.ast.binary_expr import BinaryExpr
from stone.token.id_token import IdToken
from stone.token.str_token import StrToken


class TestBinaryExpr(StoneTestBase):

    def setUp(self):
        super(TestBinaryExpr, self).setUp()
        self.be = BinaryExpr([ASTLeaf(IdToken(1, "foo")), ASTLeaf(IdToken(1, "+")), ASTLeaf(StrToken(1, "sample"))])

    def test_left(self):
        self.assertASTLeafEqual(self.be.left(), ASTLeaf(IdToken(1, "foo")))

    def test_operator(self):
        self.assertEqual(self.be.operator(), "+")

    def test_right(self):
        self.assertASTLeafEqual(self.be.right(), ASTLeaf(StrToken(1, "sample")))
