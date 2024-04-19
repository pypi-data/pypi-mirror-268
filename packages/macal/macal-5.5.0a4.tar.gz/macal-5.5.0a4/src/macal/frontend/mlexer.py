# -*- coding: utf-8 -*-
#
# Product:   Macal DSL
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      2024-03-22
#
# Copyright 2024 Westcon-Comstor
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# SPDX-License-Identifier: MIT
#

# mlexer.py is a simple lexer for Macal DSL

from enum import Enum, auto
from collections import deque
from macal.mexceptions import SyntaxError
from macal.frontend.ast.metadata import NodeMetadata
import re
import sys
import re

TAB_SIZE = 4


class TokenKind(Enum):
    IF = auto()  # Keywords
    ELIF = auto()
    ELSE = auto()
    FOREACH = auto()
    WHILE = auto()
    CONTINUE = auto()
    BREAK = auto()
    RETURN = auto()
    SELECT = auto()
    DISTINCT = auto()
    AS = auto()
    FROM = auto()
    WHERE = auto()
    ORDER = auto()
    MERGE = auto()
    INTO = auto()
    HALT = auto()
    INCLUDE = auto()
    EXTERNAL = auto()
    CONST = auto()
    SWITCH = auto()
    CASE = auto()
    DEFAULT = auto()
    RECORD = auto()
    ARRAY = auto()
    TYPE = auto()
    TYPES = auto()
    ISTYPE = auto()
    OPEN_PAREN = auto()
    CLOSE_PAREN = auto()
    OPEN_BRACE = auto()
    CLOSE_BRACE = auto()
    OPEN_BRACKET = auto()
    CLOSE_BRACKET = auto()
    COMMA = auto()
    DOT = auto()
    SEMICOLON = auto()
    COLON = auto()
    QUESTION = auto()
    AMPERSAND = auto()
    DOLLAR = auto()
    EOF = auto()
    ASSIGN = auto()
    BINARYOPERATOR = auto()
    UNARYOPERATOR = auto()
    IDENTIFIER = auto()
    STRING = auto()
    INTEGER = auto()
    FLOAT = auto()
    OBJECT = auto()
    COMMENT = auto()
    AND = auto()
    OR = auto()
    NOT = auto()
    XOR = auto()
    FN = auto()
    _INIT = auto()


class Token:
    def __init__(self) -> None:
        self.kind: TokenKind = TokenKind._INIT
        self.lexeme: str = ""  # the actual token text
        self.line: int = 0
        self.column: int = 0

    def __str__(self) -> str:
        txt = self.lexeme
        if self.kind == TokenKind.STRING:
            txt = f'"{txt}"'
        return f"{self.format_position()} {self.format_kind()} {txt}"

    def __repr__(self) -> str:
        return self.__str__()

    def format_position(self, digits: int = 4) -> str:
        line_str = str(self.line).rjust(digits)
        column_str = str(self.column).rjust(digits)
        return f"{line_str}:{column_str}"

    def format_kind(self, spaces: int = 16) -> str:
        return self.kind.name.ljust(spaces)

    def json(self) -> dict:
        return {
            "kind": self.kind.name,
            "lexeme": self.lexeme,
            "line": self.line,
            "column": self.column,
        }


class Lexer:
    def __init__(self) -> None:
        self.tokens: list[Token] = []
        self.index: int = 0  # current token index
        self.line: int = 1
        self.column: int = 1
        self.source: str = ""
        self.length: int = 0
        self.type_keywords: dict[str, TokenKind] = {
            "bool": TokenKind.TYPE,
            "int": TokenKind.TYPE,
            "integer": TokenKind.TYPE,
            "float": TokenKind.TYPE,
            "string": TokenKind.TYPE,
            "params": TokenKind.TYPE,
            "variable": TokenKind.TYPE,
            "function": TokenKind.TYPE,
        }
        self.Keywords: dict[str, TokenKind] = {
            "if": TokenKind.IF,
            "elif": TokenKind.ELIF,
            "else": TokenKind.ELSE,
            "foreach": TokenKind.FOREACH,
            "while": TokenKind.WHILE,
            "continue": TokenKind.CONTINUE,
            "break": TokenKind.BREAK,
            "return": TokenKind.RETURN,
            "select": TokenKind.SELECT,
            "distinct": TokenKind.DISTINCT,
            "as": TokenKind.AS,
            "from": TokenKind.FROM,
            "where": TokenKind.WHERE,
            "order": TokenKind.ORDER,
            "merge": TokenKind.MERGE,
            "into": TokenKind.INTO,
            "halt": TokenKind.HALT,
            "include": TokenKind.INCLUDE,
            "external": TokenKind.EXTERNAL,
            "const": TokenKind.CONST,
            "switch": TokenKind.SWITCH,
            "case": TokenKind.CASE,
            "default": TokenKind.DEFAULT,
            "record": TokenKind.RECORD,
            "array": TokenKind.ARRAY,
            "and": TokenKind.AND,
            "or": TokenKind.OR,
            "not": TokenKind.NOT,
            "xor": TokenKind.XOR,
            "object": TokenKind.OBJECT,
            "Type": TokenKind.TYPES,
            "type": TokenKind.TYPES,
            "IsRecord": TokenKind.ISTYPE,
            "IsArray": TokenKind.ISTYPE,
            "IsFunction": TokenKind.ISTYPE,
            "IsString": TokenKind.ISTYPE,
            "IsInteger": TokenKind.ISTYPE,
            "IsInt": TokenKind.ISTYPE,
            "IsFloat": TokenKind.ISTYPE,
            "IsBool": TokenKind.ISTYPE,
            "IsObject": TokenKind.ISTYPE,
            "isRecord": TokenKind.ISTYPE,
            "isArray": TokenKind.ISTYPE,
            "isFunction": TokenKind.ISTYPE,
            "isString": TokenKind.ISTYPE,
            "isInteger": TokenKind.ISTYPE,
            "isInt": TokenKind.ISTYPE,
            "isFloat": TokenKind.ISTYPE,
            "isBool": TokenKind.ISTYPE,
            "isObject": TokenKind.ISTYPE,
        }
        self.lexer_state: str = "init"

    @staticmethod
    def MakeToken(lexeme: str, kind: TokenKind, line: int, column: int) -> Token:
        token = Token()
        token.lexeme = lexeme
        token.kind = kind
        token.line = line
        token.column = column
        return token

    @staticmethod
    def is_alpha(c: str) -> bool:
        return c.isalpha() or c == "_"

    @staticmethod
    def is_digit(c: str) -> bool:
        return c.isdigit()

    @staticmethod
    def is_alnum(c: str) -> bool:
        return c.isalnum() or c == "_"

    @staticmethod
    def is_whitespace(c: str) -> bool:
        return c.isspace()

    @staticmethod
    def is_newline(c: str) -> bool:
        return c == "\n"

    def is_tab(self, c: str) -> bool:
        return c == "\t"

    def shift(self) -> str:
        self.column += 1
        if self.index > self.length:
            return "\0"
        c = self.source[self.index]
        self.index += 1
        return c

    def at(self, offset=0) -> str:
        if self.index + offset >= self.length:
            return "\0"
        return self.source[self.index + offset]

    def eof(self) -> bool:
        return self.at() == "\0"

    def start(self) -> tuple[int, int, int]:
        return self.index, self.line, self.column

    def skip_whitespace(self) -> None:
        while not self.eof() and self.is_whitespace(self.at()):
            c = self.shift()
            if self.is_newline(c):
                self.line += 1
                self.column = 1
            if self.is_tab(c):
                self.column += TAB_SIZE - 1

    def lex_identifier(self) -> Token:
        start = self.start()
        while self.is_alnum(self.at()):
            self.shift()
        lexeme = self.source[start[0] : self.index]
        kind = self.type_keywords.get(lexeme, None)
        if kind is None:
            kind = self.Keywords.get(lexeme, TokenKind.IDENTIFIER)
        return self.MakeToken(lexeme, kind, start[1], start[2])

    @staticmethod
    def split_string_with_braces(input_str: str) -> list[str]:
        parts: list[str] = []
        inside_curly_braces = False
        current_part = ""
        for char in input_str:
            if char == "{":
                if inside_curly_braces is True:
                    # Nested curly braces, which means an escape.
                    current_part = f"{parts.pop()}{{{{"
                    inside_curly_braces = False
                    continue
                # Start of curly braces
                if len(current_part) > 0:
                    parts.append(current_part)
                    current_part = ""
                inside_curly_braces = True
                current_part += char
            elif char == "}" and inside_curly_braces is True:
                # End of curly braces
                inside_curly_braces = False
                current_part += char
                parts.append(current_part)
                current_part = ""
            else:
                # Other characters
                current_part += char

        # Add the last part (if any)
        if len(current_part) > 0:
            parts.append(current_part)

        return parts

    def _lex_string(self) -> str:
        start = self.start()
        term = self.shift()
        c = "\0"
        while not self.eof() and self.at() != term:
            c = self.shift()
            if self.is_newline(c):
                self.line += 1
                self.column = 1
            if self.is_tab(c):
                self.column += TAB_SIZE - 1
            if self.at() == term and c == "\\":
                self.shift()  # skip the terminator because it was escaped.
        if self.at() != term:
            raise SyntaxError(
                "Unbalanced string",
                NodeMetadata(start[1], start[2], self.filename),
            )
        self.shift()  # skip the terminator
        return self.source[start[0] : self.index]

    def _lex_interpolation_string(self) -> str:
        start = self.start()
        term = self.shift()
        c = "\0"
        in_expr = False
        while not self.eof() and self.at() != term:
            c = self.shift()
            if self.is_newline(c):
                self.line += 1
                self.column = 1
            if self.is_tab(c):
                self.column += TAB_SIZE - 1
            if c == "{" and self.at() == "{":
                self.shift()
            if c == "}" and self.at() == "}":
                self.shift()
            if c == "{" and self.at() != "{" and not in_expr:
                in_expr = True
            if c == "}" and self.at() != "}" and in_expr:
                in_expr = False

            if c == "\\" and self.at() == term:
                self.shift()  # skip the terminator because it was escaped.
            if self.at() == term and in_expr:
                self.shift()  # skip the terminator because it's inside an expression

        if self.at() != term:
            raise SyntaxError(
                "Unbalanced string",
                NodeMetadata(start[1], start[2], self.filename),
            )
        self.shift()  # skip the terminator
        return self.source[start[0] : self.index]

    def scan_string(self, istr: str, l: int, c: int) -> tuple[int, int]:
        for ch in istr:
            if ch == "\n":
                l += 1
                c = 1
            if ch == "\t":
                c += TAB_SIZE - 1
            c += 1
        return l, c

    def lex_string_interpolation(self) -> Token:
        self.shift()  # skip the $
        start = self.start()
        tokens: list[Token] = []
        start = self.start()
        istr = self._lex_interpolation_string()
        if len(istr) >= 2:
            istr = istr[1:-1]  # Remove the quotes
        parts = self.split_string_with_braces(istr)

        l = start[1]
        c = start[2]
        for part in parts:
            ol = l
            oc = c
            l, c = self.scan_string(part, l, c)
            if (
                part.startswith("{")
                and part.endswith("}")
                and not part.startswith("{{")
                and not part.endswith("}}")
            ):
                part = part[1:-1]
                lexer = Lexer()
                ltokens = lexer.lex(part, self.filename)
                if len(tokens) > 0:
                    tokens.append(
                        self.MakeToken("+.", TokenKind.BINARYOPERATOR, ol, oc)
                    )
                for tok in ltokens[:-1]:  # Skip the EOF token
                    tok.line += ol - 1
                    tok.column += oc - 1
                    tokens.append(tok)
            else:
                if len(tokens) > 0:
                    tokens.append(
                        self.MakeToken("+.", TokenKind.BINARYOPERATOR, ol, oc)
                    )
                tokens.append(self.MakeToken(part, TokenKind.STRING, ol, oc))
        for token in tokens[:-1]:
            self.tokens.append(token)
        return tokens[-1]

    def lex_string(self) -> Token:
        start = self.start()
        istr = self._lex_string()
        if len(istr) >= 2:
            istr = istr[1:-1]  # Remove the quotes
        return self.MakeToken(istr, TokenKind.STRING, start[1], start[2])

    def lex_number(self) -> Token:
        start = self.start()
        while self.is_digit(self.at()):
            self.shift()
        if self.at() == ".":
            self.shift()
            while self.is_digit(self.at()):
                self.shift()
            return self.MakeToken(
                self.source[start[0] : self.index],
                TokenKind.FLOAT,
                start[1],
                start[2],
            )
        return self.MakeToken(
            self.source[start[0] : self.index],
            TokenKind.INTEGER,
            start[1],
            start[2],
        )

    def lex_short_comment(self) -> Token:
        start = self.start()
        c = self.shift()  # skip the / or #
        if c == "/":
            self.shift()  # skip the /
        while not self.eof() and not self.is_newline(self.at()):
            self.shift()
        return self.MakeToken(
            self.source[start[0] : self.index],
            TokenKind.COMMENT,
            start[1],
            start[2],
        )

    def lex_long_comment(self) -> Token:
        start = self.start()
        self.shift()  # skip the /
        self.shift()  # skip the *
        while not self.eof() and not (self.at() == "*" and self.at(1) == "/"):
            c = self.shift()
            if self.is_newline(c):
                self.line += 1
                self.column = 1
        self.shift()  # skip the *
        self.shift()  # skip the /
        return self.MakeToken(
            self.source[start[0] : self.index],
            TokenKind.COMMENT,
            start[1],
            start[2],
        )

    def lex_token(self) -> Token:
        start = self.start()
        if self.eof():
            return self.MakeToken("", TokenKind.EOF, start[1], start[2])
        c = self.at()
        if self.is_alpha(c):
            return self.lex_identifier()
        if self.is_digit(c):
            return self.lex_number()
        if c == '"' or c == "'":
            return self.lex_string()
        if c == "/":
            if self.at(1) == "/":
                return self.lex_short_comment()
            if self.at(1) == "*":
                return self.lex_long_comment()
            op = self.shift()
            if self.at() == "=":
                return self.MakeToken(
                    op + self.shift(), TokenKind.BINARYOPERATOR, start[1], start[2]
                )
            return self.MakeToken(op, TokenKind.BINARYOPERATOR, start[1], start[2])
        if c == "#":
            return self.lex_short_comment()
        if c == "(":
            return self.MakeToken(
                self.shift(), TokenKind.OPEN_PAREN, start[1], start[2]
            )
        if c == ")":
            return self.MakeToken(
                self.shift(), TokenKind.CLOSE_PAREN, start[1], start[2]
            )
        if c == "{":
            return self.MakeToken(
                self.shift(), TokenKind.OPEN_BRACE, start[1], start[2]
            )
        if c == "}":
            return self.MakeToken(
                self.shift(), TokenKind.CLOSE_BRACE, start[1], start[2]
            )
        if c == "[":
            return self.MakeToken(
                self.shift(), TokenKind.OPEN_BRACKET, start[1], start[2]
            )
        if c == "]":
            return self.MakeToken(
                self.shift(), TokenKind.CLOSE_BRACKET, start[1], start[2]
            )
        if c == ",":
            return self.MakeToken(self.shift(), TokenKind.COMMA, start[1], start[2])
        if c == ";":
            return self.MakeToken(self.shift(), TokenKind.SEMICOLON, start[1], start[2])
        if c == ":":
            return self.MakeToken(self.shift(), TokenKind.COLON, start[1], start[2])
        if c == "?":
            return self.MakeToken(self.shift(), TokenKind.QUESTION, start[1], start[2])
        if c == "&":
            tok = self.shift()
            if self.at() == "&":
                self.shift()
                return self.MakeToken("&&", TokenKind.AND, start[1], start[2])
            return self.MakeToken(tok, TokenKind.AND, start[1], start[2])
        if c == "|":
            tok = self.shift()
            if self.at() == "|":
                self.shift()
                return self.MakeToken("||", TokenKind.OR, start[1], start[2])
            return self.MakeToken(tok, TokenKind.OR, start[1], start[2])
        if c == "$":
            return self.lex_string_interpolation()
        if (
            c == "+"
            or c == "-"
            or c == "*"
            or c == "%"
            or c == "^"
            or c == "!"
            or c == "<"
            or c == ">"
            or c == "."  # for string concatenation or object member expressions
        ):
            op = self.shift()
            if self.at() == "=":
                self.shift()  # skip the =
                return self.MakeToken(
                    f"{op}=", TokenKind.BINARYOPERATOR, start[1], start[2]
                )
            elif c == ".":
                return self.MakeToken(c, TokenKind.DOT, start[1], start[2])
            elif c == "*" and self.at() == "*":
                self.shift()
                return self.MakeToken(
                    "**", TokenKind.BINARYOPERATOR, start[1], start[2]
                )
            elif (c == "-" and self.at() == "-") or (c == "+" and self.at() == "+"):
                u = self.shift()
                return self.MakeToken(
                    f"{op}{u}", TokenKind.UNARYOPERATOR, start[1], start[2]
                )

            return self.MakeToken(op, TokenKind.BINARYOPERATOR, start[1], start[2])
        if c == "=":
            op = self.shift()
            if self.at() == "=":
                return self.MakeToken(
                    op + self.shift(), TokenKind.BINARYOPERATOR, start[1], start[2]
                )
            if self.at() == ">":
                return self.MakeToken(
                    op + self.shift(), TokenKind.FN, start[1], start[2]
                )
            return self.MakeToken(op, TokenKind.ASSIGN, start[1], start[2])

        em = c
        if c == "\n":
            em = "'<lf>'"
        if c == "\r":
            em = "'<cr>'"
        if c == "\t":
            em = "'<tab>'"
        if c == "\0":
            em = "'<eof>'"
        if c == " ":
            em = "'<space>'"
        raise SyntaxError(
            f"Unexpected character {em}",
            NodeMetadata(start[1], start[2], self.filename),
        )

    def lex(self, source: str, filename: str) -> list[Token]:
        self.source = source
        self.length = len(source)
        self.filename = filename
        self.lexer_state = "lexing"
        while not self.eof():
            self.skip_whitespace()
            token = self.lex_token()
            self.tokens.append(token)
        if self.tokens[-1].kind != TokenKind.EOF:
            self.tokens.append(
                self.MakeToken("", TokenKind.EOF, self.line, self.column)
            )
        self.lexer_state = "done"
        return self.tokens

    def print(self) -> None:
        print()
        print("Tokens:")
        for token in self.tokens:
            print(token)
        print()
