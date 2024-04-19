# -*- coding: utf-8 -*-
#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      2024-04-10
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

import pathlib
import sys
from typing import Optional, Any
from macal.__about__ import __version__
from macal.frontend.mparser import Parser
from macal.runtime.minterpreter import Interpreter
from macal.runtime.menvironment import Env
from macal.mexceptions import SyntaxError, RuntimeError, RuntimeErrorLC
from macal.frontend.mparserstate import ParserSymbol, ParserState
from macal.runtime.values import (
    IRuntimeValue,
    NilValue,
    BooleanValue,
    IntegerValue,
    FloatValue,
    StringValue,
    RecordObject,
    ArrayObject,
    NodeMetadata,
    HaltValue,
)


class Macal:

    def __init__(self, search_paths: list[str] = []) -> None:
        self.__environment: Env = Env.CreateGlobalEnv()
        self.__parser_state = ParserState(
            name="global", parent=None, filename=""
        )  # global environment state.
        self._search_paths: list[str] = search_paths
        self._version: str = __version__

    @property
    def version(self) -> str:
        return self._version

    @property
    def paths(self) -> list[str]:
        return self._search_paths

    def AddPath(self, path: str) -> None:
        self._search_paths.append(path)

    def RemovePath(self, path: str) -> None:
        self._search_paths.remove(path)

    def _convert(self, value: Any, env: Env) -> IRuntimeValue:
        """Converts a Python value to a Macal value."""
        if value is None:
            return NilValue()
        if isinstance(value, bool):
            return BooleanValue(value)
        if isinstance(value, int):
            return IntegerValue(value)
        if isinstance(value, float):
            return FloatValue(value)
        if isinstance(value, str):
            return StringValue(value, NodeMetadata.new())
        if isinstance(value, dict):
            record = RecordObject(NodeMetadata.new())
            for key, val in value.items():
                record.properties[key] = self._convert(val, env)
            return record
        if isinstance(value, list):
            array = ArrayObject(NodeMetadata.new())
            for val in value:
                array.append(self._convert(val, env))
            return array
        raise RuntimeError(f"Unknown Python value type: {type(value)}")

    def RegisterVariable(self, name: str, value: Any) -> None:
        """Add a variable to the global environment."""
        symbol = ParserSymbol(name, NodeMetadata.new(), is_global=True, is_const=False)
        self.__parser_state.symbols.append(symbol)
        self.__environment.DeclareVar(
            name, value=self._convert(value, env=self.__environment)
        )

    def RegisterConstant(self, name: str, value: Any) -> None:
        """Add a const to the global environment."""
        symbol = ParserSymbol(name, NodeMetadata.new(), is_global=True, is_const=True)
        self.__parser_state.symbols.append(symbol)
        self.__environment.DeclareVar(
            name, value=self._convert(value, env=self.__environment)
        )

    def AssignVariable(self, name: str, value: Any) -> None:
        """Assign a value to a variable in the global environment."""

        self.__environment.AssignVar(
            name=name, value=self._convert(value, env=self.__environment), meta=None
        )

    def Run(self, filename: str) -> None:
        """Run a Macal file."""
        try:
            self.RunUnsafe(filename=filename, debug=False)
        except RuntimeErrorLC as e:
            print(f"{e}")
            sys.exit(1)
        except SyntaxError as e:
            print(f"{e}")
            sys.exit(1)
        except RuntimeError as e:
            print(f"{e}")
            sys.exit(1)

    def RunUnsafe(self, filename: str, debug: bool = False) -> None:
        """Run a Macal file in debug mode, without any crash protections."""
        with open(filename, "r") as f:
            source = f.read()
        self.__parser_state.filename = filename
        parser = Parser(filename)
        program = parser.ProduceAST(source, state=self.__parser_state, debug=debug)
        interpreter = Interpreter()
        for path in self._search_paths:
            interpreter.add_path(str(pathlib.Path(path).absolute()))
        ret = interpreter.evaluate(program, self.__environment)
        if isinstance(ret, HaltValue):
            sys.exit(ret.value.value)
