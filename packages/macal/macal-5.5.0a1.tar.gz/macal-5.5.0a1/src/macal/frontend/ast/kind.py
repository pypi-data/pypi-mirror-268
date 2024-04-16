# -*- coding: utf-8 -*-
#
# Product:   Macal
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

from enum import Enum, auto


class NodeKind(Enum):
    """Enumeration of AST node kinds."""

    # Statements
    PROGRAM = auto()
    VAR_DECL = auto()
    FUNC_DECL = auto()
    STMT_RETURN = auto()
    STMT_CONTINUE = auto()
    STMT_BREAK = auto()
    STMT_HALT = auto()
    STMT_IF = auto()
    STMT_ELIF = auto()
    STMT_ELSE = auto()
    STMT_WHILE = auto()
    STMT_FOREACH = auto()
    STMT_SELECT = auto()
    STMT_SWITCH = auto()
    STMT_CASE = auto()
    STMT_DEFAULT = auto()
    STMT_INCLUDE = auto()
    STMT_TYPE = auto()
    STMT_IS_TYPE = auto()

    # Expressions
    EXPR_ASSIGN = auto()
    EXPR_MEMBER = auto()
    EXPR_CALL = auto()
    EXPR_BINARY = auto()
    EXPR_UNARY = auto()

    # Literals
    LIT_INT = auto()
    LIT_FLOAT = auto()
    LIT_STRING = auto()
    LIT_STRING_INTERPOLATION = auto()
    LIT_IDENT = auto()
    LIT_OBJECT = auto()
    LIT_PROPERTY = auto()
    LIT_LIBRARY = auto()
    LIT_ARRAY = auto()
    LIT_RECORD = auto()
    LIT_NEW_RECORD = auto()
    LIT_NEW_ARRAY = auto()

    def __str__(self):
        return self.value


class ObjectKind(Enum):
    """Enumeration of object kinds."""

    OBJECT = auto()
    ARRAY = auto()
    RECORD = auto()
    INTERPOLATION = auto()

    def __str__(self):
        return self.value
