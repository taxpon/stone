# -*- coding: utf-8 -*-

import string
import re
from typing import List
from stone.file import File
from stone.token.token import Token, EOF, EOL
from stone.token.num_token import NumToken
from stone.token.str_token import StrToken
from stone.token.id_token import IdToken


class Lexer(object):

    punc_pat = r"[{}]".format(string.punctuation)

    pat_comment = r"//.*"
    pattern = re.compile(r"\s*((//.*)|(\d+)|(\"(\\\\\"|\\\\\\\\|\\\\n|[^\"])*\")|"
                         r"[A-Za-z][]A-Za-z0-9]*|==|<=|>=|&&|\|\||{punc})?".format(punc=punc_pat))

    def __init__(self, fo: File):
        self.fo = fo
        self.has_more = True
        self.queue = []  # type: List[Token]

    def read(self) -> Token:
        if self.__fill_queue(0):
            return self.queue.pop(0)
        else:
            return EOF

    def peek(self, i: int) -> Token:
        if self.__fill_queue(i):
            return self.queue[i]
        else:
            return EOF

    def __fill_queue(self, i: int) -> bool:
        while i >= len(self.queue):
            if self.has_more:
                self._read_line()
            else:
                return False
        return True

    def _read_line(self):
        line = self.fo.readline()
        if not line:
            self.has_more = False
            return

        pos = 0
        end_pos = len(line)
        while pos < end_pos:
            m = self.pattern.match(line[pos:end_pos])
            self._add_token(self.fo.line_number, m)
            pos += m.end()
        self.queue.append(IdToken(self.fo.line_number, EOL))

    def _add_token(self, line_number: int, matcher):
        groups = matcher.groups()
        m = groups[0]

        if m is not None:  # if not space
            if groups[1] is None:  # if not comment
                if groups[2] is not None:
                    token = NumToken(line_number=line_number, value=int(groups[2]))
                elif groups[3] is not None:
                    token = StrToken(line_number=line_number, text=self._to_string(groups[3]))
                else:
                    token = IdToken(line_number=line_number, _id=m)
                self.queue.append(token)

    def _to_string(self, s: str):
        l = len(s) - 1
        sb = ""
        for i in range(1, l):
            c = s[i]
            if c == '\\' and i + 1 < len:
                c2 = s[i + 1]
                if c2 == '"' or '\\':
                    c = s[i + 2]
                    i += 1
                elif c2 == "n":
                    i += 1
                    c = "\n"
            sb += c
        return sb
