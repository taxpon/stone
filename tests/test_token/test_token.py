# -*- coding: utf-8 -*-

from tests.base_test import StoneTestBase
from stone.token.token import Token
from stone.errors import StoneException


class TestToken(StoneTestBase):

    def setUp(self):
        super(TestToken, self).setUp()
        self.token = Token(10)

    def test_line_number(self):
        self.assertEqual(self.token.line_number, 10)

    def test_number(self):
        with self.assertRaises(StoneException):
            _ = self.token.number

    def test_text(self):
        self.assertEqual("", self.token.text)

    def test_is_identifier(self):
        self.assertFalse(self.token.is_id())

    def test_is_number(self):
        self.assertFalse(self.token.is_num())

    def test_is_string(self):
        self.assertFalse(self.token.is_str())
