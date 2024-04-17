#!/usr/bin/env python
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

# mrepl.py is a simple file runner for Macal DSL 6.0.0

import pathlib
import sys
import argparse
from macal.frontend.mlexer import Lexer
from macal.__about__ import __version__
from macal.frontend.mparser import Parser
from macal.runtime.minterpreter import Interpreter
from macal.runtime.menvironment import Env
from macal.mexceptions import SyntaxError, RuntimeError, SyntaxError, RuntimeErrorLC
import json


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Macal DSL file runner")
    parser.add_argument(
        "-d",
        "--debug",
        help="Print debug information",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-dd",
        "--debug_debug",
        help="Print more debug information",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-dv",
        "--debug_var",
        help="Show extra debug information about a specific variable",
        default=None,
    )
    parser.add_argument(
        "--debug_verbose",
        help="Print verbose debug information",
        action="store_true",
        default=False,
    )
    parser.add_argument(
        "-l", "--lex_only", help="Only lex the file", action="store_true"
    )
    parser.add_argument(
        "-p", "--parse_only", help="Only parse the file", action="store_true"
    )
    parser.add_argument("-s", "--script", help="Macal DSL file to run")
    parser.add_argument(
        "--lib", help="Macal DSL library path to add to the search path"
    )
    parser.add_argument(
        "-v", "--version", help="Print the version of Macal DSL", action="store_true"
    )

    parser.add_argument("file", nargs="?", help="Alias for -s/--script")
    return parser.parse_args()


def run_file(file: str, args: argparse.Namespace) -> None:
    lexer = None
    parser = None
    interpreter = None
    program = None
    try:
        current_dir = pathlib.Path(file).parent.absolute()
        print(current_dir)
        with open(file, "r") as f:
            source = f.read()
        if args.lex_only:
            lexer = Lexer()
            lexer.lex(source, file)
            if args.debug:
                lexer.print()
            sys.exit(0)
        parser = Parser(file)
        program = parser.ProduceAST(source, args.debug)
        if args.debug:
            parser.print(program)
        if args.parse_only:
            sys.exit(0)
        interpreter = Interpreter()

        interpreter.add_path(str(current_dir))
        if args.lib:
            interpreter.add_path(str(pathlib.Path(args.lib).absolute()))
        interpreter.interpreter_state = "running"
        env = Env.CreateGlobalEnv()
        result = interpreter.evaluate(program, env)
        interpreter.interpreter_state = "done"
        if args.debug:
            interpreter.print(result)
    except Exception as e:
        raise e
    finally:
        if args.debug_debug or args.debug_var or args.debug_verbose:
            print()
            print("Debugging information:")
            print(f"Current directory: {current_dir}")
            print(f"Library path: {args.lib}")
            print(f"Macal DSL version: {__version__}")
            print(f"Macal DSL file: {file}")
            print(f"Macal DSL script: {args.script}")
            print(f"Macal DSL parse only: {args.parse_only}")
            print(f"Macal DSL lex only: {args.lex_only}")
            print(f"Macal DSL debug: {args.debug}")
            print(f"Macal DSL debug debug: {args.debug_debug}")
            print(f"Macal DSL debug var: {args.debug_var}")
            if args.lex_only:
                print(f"Lexer State: {lexer.lexer_state}")  # type: ignore
            elif args.parse_only:
                print(f"Lexer State: {parser._lexer_state}")  # type: ignore
                print(f"Parser State: {parser._parser_state}")  # type: ignore
            else:
                print(f"Lexer State: {parser._lexer_state}")  # type: ignore
                if parser._lexer_state == "done":  # type: ignore
                    print()
                    print("Lexer Tokens:")
                    for token in parser.tokens:  # type: ignore
                        print(token)
                    print()
                print(f"Parser State: {parser._parser_state}")  # type: ignore
                print(f"Parser Length: {parser._length}")  # type: ignore
                print(f"Parser Position: {parser._current}")  # type: ignore
                print()
                print("Parser Symbols:")
                for symbol in parser.symbols:  # type: ignore
                    print(symbol)
                print()
                print(f"Interpreter State: {interpreter.interpreter_state}")  # type: ignore
                if args.debug_var:
                    print()
                    print(f"Variable {args.debug_var}:")
                    var = env.FindVar(args.debug_var)
                    if var is not None:
                        try:
                            print(json.dumps(var.json(), indent=4))
                        except Exception:
                            print(var.json())
                    else:
                        print(f"Variable {args.debug_var} not found")
                    print()
            print()


def execute_file(file: str, args: argparse.Namespace) -> None:
    if args.debug:
        print(f"Running file: {file}")
        run_file(file, args)
    else:
        try:
            run_file(file, args)
        except RuntimeError as e:
            print(f"{e}")
            sys.exit(1)
        except RuntimeErrorLC as e:
            print(f"{e}")
            sys.exit(1)
        except SyntaxError as e:
            print(f"{e}")
            sys.exit(1)


def main():
    args = parse_args()
    if args.version:
        print(f"Macal DSL {__version__}")
        sys.exit(0)
    if args.script:
        execute_file(args.script, args)
    elif args.file:
        execute_file(args.file, args)
    else:
        print("No file specified")
        sys.exit(1)


if __name__ == "__main__":
    main()
