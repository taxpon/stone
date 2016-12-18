# -*- coding: utf-8 -*-

from tests.base_test import StoneTestBase
from stone.token.num_token import NumToken


class TestNumToken(StoneTestBase):

    def setUp(self):
        self.num_token = NumToken(10, 20)

    def test_number(self):
        self.assertEqual(self.num_token.number, 20)

    def test_is_num(self):
        self.assertTrue(self.num_token.is_num())
