# -*- coding: utf-8 -*-

from tests.base_test import StoneTestBase
from stone.ast.astleaf import ASTLeaf
from stone.ast.astlist import ASTList
from stone.token.str_token import StrToken


dummy_list = [ASTLeaf(StrToken(1, "first")), ASTLeaf(StrToken(1, "second")), ASTLeaf(StrToken(2, "third"))]


class TestAstList(StoneTestBase):

    def setUp(self):
        super(TestAstList, self).setUp()
        self.list = ASTList(dummy_list)

    def test_child(self):
        self.assertEqual(self.list.child(0), dummy_list[0])
        self.assertEqual(self.list.child(1), dummy_list[1])
        self.assertEqual(self.list.child(2), dummy_list[2])

    def test_num_children(self):
        self.assertEqual(self.list.num_children(), 3)

    def test_children(self):
        self.assertEqual(self.list.children(), dummy_list)

    def test_to_string(self):
        self.assertEqual(self.list.to_string(), "(first second third)")

    def location(self):
        self.assertEqual(self.list.location(), "at 1 first")
