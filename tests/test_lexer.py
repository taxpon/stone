# -*- coding: utf-8 -*-

import io
from nose_parameterized import parameterized
from tests.base_test import StoneTestBase
from stone.lexer import Lexer
from stone.file import File
from stone.token.token import EOF, EOL, Token
from stone.token.num_token import NumToken
from stone.token.str_token import StrToken
from stone.token.id_token import IdToken


class TestLexerBase(StoneTestBase):
    pass


class TestLexer(TestLexerBase):

    @parameterized.expand([
        ("  // some comment", "// some comment"),
        ("// some comment", "// some comment"),
        ("// some comment//123", "// some comment//123")
    ])
    def test_pattern_comment(self, value, answer):
        m = Lexer.pattern.match(value)
        self.assertIsNotNone(m)
        self.assertEqual(m.groups()[0], answer)
        self.assertEqual(m.groups()[1], answer)
        self.assertEqual(m.groups()[2], None)
        self.assertEqual(m.groups()[3], None)
        self.assertEqual(m.groups()[4], None)
        self.assertEqual(m.end(), len(value))

    @parameterized.expand([
        (" 123", "123"),
        ("123", "123"),
        ("0", "0"),
        ("  0000", "0000"),
    ])
    def test_pattern_num(self, value, answer):
        m = Lexer.pattern.match(value)
        self.assertIsNotNone(m)
        self.assertEqual(m.groups()[0], answer)
        self.assertEqual(m.groups()[1], None)
        self.assertEqual(m.groups()[2], answer)
        self.assertEqual(m.groups()[3], None)
        self.assertEqual(m.groups()[4], None)

    @parameterized.expand([
        ('  "abc"', '"abc"')
    ])
    def test_pattern_str(self, value, answer):
        m = Lexer.pattern.match(value)
        self.assertIsNotNone(m)
        self.assertEqual(m.groups()[0], answer)
        self.assertEqual(m.groups()[1], None)
        self.assertEqual(m.groups()[2], None)
        self.assertEqual(m.groups()[3], answer)
        self.assertEqual(m.groups()[4], answer[-2])

    @parameterized.expand([
        ('  abc', 'abc'),
        ('  ==', '=='),
        ('  ||', '||'),
        ('  !', '!'),
        ('  &', '&'),
        ('  %', '%'),
    ])
    def test_pattern_id(self, value, answer):
        m = Lexer.pattern.match(value)
        self.assertIsNotNone(m)
        self.assertEqual(m.groups()[0], answer)
        self.assertEqual(m.groups()[1], None)
        self.assertEqual(m.groups()[2], None)
        self.assertEqual(m.groups()[3], None)
        self.assertEqual(m.groups()[4], None)

    def test_read_1(self):
        l = Lexer(File(io.StringIO("aaa = 123\n")))
        self.assertTokenEqual(l.read(), IdToken(1, "aaa"))
        self.assertTokenEqual(l.read(), IdToken(1, "="))
        self.assertTokenEqual(l.read(), NumToken(1, 123))
        self.assertTokenEqual(l.read(), IdToken(1, EOL))
        self.assertTokenEqual(l.read(), EOF)

    def test_read_2(self):
        l = Lexer(File(io.StringIO('aaa = 123\nif a = b {print("Hello")}')))
        self.assertTokenEqual(l.read(), IdToken(1, "aaa"))
        self.assertTokenEqual(l.read(), IdToken(1, "="))
        self.assertTokenEqual(l.read(), NumToken(1, 123))
        self.assertTokenEqual(l.read(), IdToken(1, EOL))
        self.assertTokenEqual(l.read(), IdToken(2, "if"))
        self.assertTokenEqual(l.read(), IdToken(2, "a"))
        self.assertTokenEqual(l.read(), IdToken(2, "="))
        self.assertTokenEqual(l.read(), IdToken(2, "b"))
        self.assertTokenEqual(l.read(), IdToken(2, "{"))
        self.assertTokenEqual(l.read(), IdToken(2, "print"))
        self.assertTokenEqual(l.read(), IdToken(2, "("))
        self.assertTokenEqual(l.read(), StrToken(2, "Hello"))
        self.assertTokenEqual(l.read(), IdToken(2, ")"))
        self.assertTokenEqual(l.read(), IdToken(2, "}"))
        self.assertTokenEqual(l.read(), IdToken(2, EOL))
        self.assertTokenEqual(l.read(), EOF)

    def test_peek_1(self):
        l = Lexer(File(io.StringIO("aaa = 123\n")))
        self.assertTokenEqual(l.peek(0), IdToken(1, "aaa"))
        self.assertTokenEqual(l.peek(1), IdToken(1, "="))
        self.assertTokenEqual(l.peek(2), NumToken(1, 123))
        self.assertTokenEqual(l.peek(3), IdToken(1, EOL))
        self.assertTokenEqual(l.peek(4), EOF)

    def test_peek_2(self):
        l = Lexer(File(io.StringIO('aaa = 123\nif a = b {print("Hello")}')))
        self.assertTokenEqual(l.peek(0), IdToken(1, "aaa"))
        self.assertTokenEqual(l.peek(1), IdToken(1, "="))
        self.assertTokenEqual(l.peek(2), NumToken(1, 123))
        self.assertTokenEqual(l.peek(3), IdToken(1, EOL))
        self.assertTokenEqual(l.peek(4), IdToken(2, "if"))
        self.assertTokenEqual(l.peek(5), IdToken(2, "a"))
        self.assertTokenEqual(l.peek(6), IdToken(2, "="))
        self.assertTokenEqual(l.peek(7), IdToken(2, "b"))
        self.assertTokenEqual(l.peek(8), IdToken(2, "{"))
        self.assertTokenEqual(l.peek(9), IdToken(2, "print"))
        self.assertTokenEqual(l.peek(10), IdToken(2, "("))
        self.assertTokenEqual(l.peek(11), StrToken(2, "Hello"))
        self.assertTokenEqual(l.peek(12), IdToken(2, ")"))
        self.assertTokenEqual(l.peek(13), IdToken(2, "}"))
        self.assertTokenEqual(l.peek(14), IdToken(2, EOL))
        self.assertTokenEqual(l.peek(15), EOF)
