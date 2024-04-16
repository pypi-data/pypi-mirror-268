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
    def __init__(self, filename: str) -> None:
        self.__filename: str = filename
        self.__environment: Env = Env.CreateGlobalEnv()
        self.__parser_state = ParserState(
            name="global", parent=None, filename=filename
        )  # global environment state.
        self.__paths: list[str] = []
        self.__version__: str = __version__

    @property
    def version(self) -> str:
        return self.__version__

    @property
    def paths(self) -> list[str]:
        return self.__paths

    def add_path(self, path: str) -> None:
        self.__paths.append(path)

    def remove_path(self, path: str) -> None:
        self.__paths.remove(path)

    def __convert(self, value: Any, env: Env) -> IRuntimeValue:
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
                record.properties[key] = self.__convert(val, env)
            return record
        if isinstance(value, list):
            array = ArrayObject(NodeMetadata.new())
            for val in value:
                array.append(self.__convert(val, env))
            return array
        raise RuntimeError(f"Unknown Python value type: {type(value)}")

    def add_variable(self, name: str, value: Any) -> None:
        """Add a variable to the global environment."""
        symbol = ParserSymbol(name, NodeMetadata.new(), is_global=True, is_const=False)
        self.__parser_state.symbols.append(symbol)
        self.__environment.DeclareVar(
            name, value=self.__convert(value, env=self.__environment)
        )

    def add_const(self, name: str, value: Any) -> None:
        """Add a const to the global environment."""
        symbol = ParserSymbol(name, NodeMetadata.new(), is_global=True, is_const=True)
        self.__parser_state.symbols.append(symbol)
        self.__environment.DeclareVar(
            name, value=self.__convert(value, env=self.__environment)
        )

    def Run(self) -> None:
        """Run a Macal file."""
        try:
            with open(self.__filename, "r") as f:
                source = f.read()
            parser = Parser(self.__filename)
            program = parser.ProduceAST(source, state=self.__parser_state)

            interpreter = Interpreter()
            for path in self.__paths:
                interpreter.add_path(str(pathlib.Path(path).absolute()))
            ret = interpreter.evaluate(program, self.__environment)
            if isinstance(ret, HaltValue):
                sys.exit(ret.value.value)
        except RuntimeErrorLC as e:
            print(f"{e}")
            sys.exit(1)
        except SyntaxError as e:
            print(f"{e}")
            sys.exit(1)
        except RuntimeError as e:
            print(f"{e}")
            sys.exit(1)

    def RunDebug(self) -> None:
        """Run a Macal file in debug mode, without any crash protections."""

        with open(self.__filename, "r") as f:
            source = f.read()
        parser = Parser(self.__filename)
        program = parser.ProduceAST(source, state=self.__parser_state, debug=True)
        interpreter = Interpreter()
        for path in self.__paths:
            interpreter.add_path(str(pathlib.Path(path).absolute()))
        ret = interpreter.evaluate(program, self.__environment)
        if isinstance(ret, HaltValue):
            sys.exit(ret.value.value)
