# -*- coding: utf-8 -*-
#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      2024-04-08
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

# Parser state keeps track of the current state of the parser, as well as the symbol table.
# It can have parent states, which are used for nested scopes.

from __future__ import annotations
from typing import Optional
from macal.frontend.mlexer import Token
from macal.frontend.ast.metadata import NodeMetadata


class ParserSymbol:
    def __init__(
        self, name: str, metadata: NodeMetadata, is_global: bool, is_const: bool = False
    ) -> None:
        self.name: str = name
        self.metadata: NodeMetadata = metadata
        self.is_global: bool = is_global
        self.is_const: bool = is_const

    def json(self) -> dict:
        return {
            "name": self.name,
            "metadata": self.metadata.json(),
            "is_global": self.is_global,
            "is_const": self.is_const,
        }


class ParserState:
    def __init__(
        self,
        parent: Optional[ParserState],
        filename: str,
        name: str,
        is_in_loop: bool = False,
        is_in_function: bool = False,
        is_in_switch: bool = False,
        is_function_definition: bool = False,
    ) -> None:
        self.name: str = name
        self.parent: Optional[ParserState] = parent
        self.filename: str = filename
        self.symbols: list[ParserSymbol] = []
        self.is_in_loop: bool = is_in_loop
        self.is_in_function: bool = is_in_function
        self.is_in_switch: bool = is_in_switch
        self.is_function_definition: bool = is_function_definition

    def reset(self):  # reset is used by the repl to reset the symbol table
        self.symbols = []
        if self.parent is not None:
            self.parent.reset()

    def is_global(self) -> bool:
        return self.parent is None

    def get_global(self) -> ParserState:
        if self.parent is not None:
            return self.parent.get_global()
        return self

    def add_symbol(self, token: Token, is_const: bool = False) -> ParserSymbol:
        symbol = ParserSymbol(
            token.lexeme,
            NodeMetadata(token.line, token.column, self.filename),
            self.is_global(),
            is_const,
        )
        self.symbols.append(symbol)
        return symbol

    def _find_symbol(self, symbol: str) -> Optional[ParserState]:
        if any(s.name == symbol for s in self.symbols):
            return self

        if self.parent is not None:
            return self.parent.find_symbol(symbol)

        return None

    def find_symbol(self, symbol: str) -> Optional[ParserState]:
        state = self._find_symbol(symbol)
        if state is not None:
            if state.name in self.name or (
                self.is_function_definition is False and self.is_in_function is False
            ):
                return state
        return None

    def get_symbol(self, symbol: str) -> Optional[ParserSymbol]:
        state = self.find_symbol(symbol)
        if state is not None:
            for s in state.symbols:
                if s.name == symbol:
                    return s
        return None

    def create_child(
        self,
        name: str,
        filename: Optional[str] = None,
        is_in_loop: bool = False,
        is_in_function: bool = False,
        is_in_switch: bool = False,
        is_function_definition: bool = False,
    ) -> ParserState:
        state = ParserState(
            name=name,
            parent=self,
            filename=filename or self.filename,
            is_in_loop=is_in_loop or self.is_in_loop,
            is_in_function=is_in_function or self.is_in_function,
            is_in_switch=is_in_switch or self.is_in_switch,
            is_function_definition=is_function_definition
            or self.is_function_definition,
        )
        return state
