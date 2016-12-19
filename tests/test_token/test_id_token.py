# -*- coding: utf-8 -*-

from tests.base_test import StoneTestBase
from stone.token.id_token import IdToken


class TestIdToken(StoneTestBase):

    def setUp(self):
        self.id_token = IdToken(10, "some_id")

    def test_text(self):
        self.assertEqual(self.id_token.text, "some_id")

    def test_is_id(self):
        self.assertTrue(self.id_token.is_id())
