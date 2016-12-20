# -*- coding: utf-8 -*-

from io import TextIOBase


class FileReadException(Exception):
    pass


class File(object):

    def __init__(self, stream: TextIOBase):
        self._line_number = 0
        self._stream = stream
        self._is_end = False

    @property
    def line_number(self) -> int:
        return self._line_number

    def readline(self) -> str:
        line = self._stream.readline()

        if self._is_end:
            raise FileReadException("You've already reached end of the file.")

        if line == "":
            self._is_end = True
        else:
            self._line_number += 1

        return line
