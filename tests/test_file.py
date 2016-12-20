# -*- coding: utf-8 -*-

import io
from tests.base_test import StoneTestBase
from stone.file import File, FileReadException


class TestFile(StoneTestBase):

    def setUp(self):
        super(TestFile, self).setUp()
        self.file = File(io.StringIO('''
first line
second line
third line
'''))

    def test_line_number(self):
        self.assertEqual(self.file.line_number, 0)
        self.file.readline()
        self.assertEqual(self.file.line_number, 1)
        self.file.readline()
        self.assertEqual(self.file.line_number, 2)

    def test_readline(self):
        line = self.file.readline()
        self.assertEqual(line, "\n")
        line = self.file.readline()
        self.assertEqual(line, "first line\n")
        line = self.file.readline()
        self.assertEqual(line, "second line\n")
        line = self.file.readline()
        self.assertEqual(line, "third line\n")
        line = self.file.readline()
        self.assertEqual(line, "")  # End of File
        with self.assertRaises(FileReadException):
            self.file.readline()
