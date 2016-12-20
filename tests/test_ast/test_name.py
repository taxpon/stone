# -*- coding: utf-8 -*-

from tests.base_test import StoneTestBase
from stone.ast.name import Name
from stone.token.str_token import StrToken


class TestName(StoneTestBase):

    def test_value(self):
        value = "sample"
        nl = Name(StrToken(1, value))
        self.assertEqual(nl.name, value)
