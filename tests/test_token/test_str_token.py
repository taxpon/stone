# -*- coding: utf-8 -*-

from tests.base_test import StoneTestBase
from stone.token.str_token import StrToken


class TestStrToken(StoneTestBase):

    def setUp(self):
        super(TestStrToken, self).setUp()
        self.str_token = StrToken(10, "test")

    def test_text(self):
        self.assertEqual(self.str_token.text, "test")

    def test_is_str(self):
        self.assertTrue(self.str_token.is_str())
