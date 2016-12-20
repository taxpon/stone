# -*- coding: utf-8 -*-

from tests.base_test import StoneTestBase
from stone.ast.number_literal import NumberLiteral
from stone.token.num_token import NumToken


class TestNumberLiteral(StoneTestBase):

    def test_value(self):
        value = 100
        nl = NumberLiteral(NumToken(1, value))
        self.assertEqual(nl.value, value)
