# -*- coding: utf-8 -*-

from tests.base_test import StoneTestBase
from stone.ast.astleaf import ASTLeaf
from stone.token.str_token import StrToken


dummy_string = "sample"


class TestASTLeaf(StoneTestBase):

    def setUp(self):
        super(TestASTLeaf, self).setUp()
        self.leaf = ASTLeaf(StrToken(1, dummy_string))

    def test_child(self):
        with self.assertRaises(IndexError):
            self.leaf.child(0)

    def test_num_children(self):
        self.assertEqual(self.leaf.num_children(), 0)

    def test_children(self):
        self.assertEqual(self.leaf.children(), [])

    def test_to_string(self):
        self.assertEqual(self.leaf.to_string(), dummy_string)

    def test_token(self):
        self.assertTokenEqual(self.leaf.token, StrToken(1, dummy_string))
