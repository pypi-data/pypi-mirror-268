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

# mrepl.py is a simple REPL for Macal


import click
import sys
import pathlib
from typing import Optional
import argparse
from macal.__about__ import __version__  # type: ignore
from macal.frontend.mparser import Parser, ParserState  # type: ignore
from macal.frontend.mlexer import Token  # type: ignore
from macal.frontend.ast.node import ProgramNode  # type: ignore

from macal.runtime.minterpreter import Interpreter  # type: ignore
from macal.runtime.menvironment import Env  # type: ignore
from macal.runtime.values import ValueType, HaltValue  # type: ignore
from macal.mexceptions import RuntimeError, SyntaxError, RuntimeErrorLC  # type: ignore

DEFAULT_HISTORY_PATH = "~/.history"

DEFAULT_CURSOR = ">"
DEFAULT_PROMPT = "macal"
COMMAND_CURSOR = "$"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Macal DSL REPL",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version="%(prog)s " + __version__,
        help="Show version information",
    )
    parser.add_argument(
        "-d", "--debug", action="store_true", help="Enable debug mode", default=False
    )
    parser.add_argument(
        "--lib",
        help="Macal DSL library path to add to the search path",
        default="./lib",
    )
    parser.add_argument(
        "--history", help="Path to the history file", default=DEFAULT_HISTORY_PATH
    )
    return parser.parse_args()


class MRepl:
    def __init__(self, alt_history_path: Optional[str] = None) -> None:
        self.__history_path: str = alt_history_path or DEFAULT_HISTORY_PATH
        self.history: list[str] = self.__load_history()
        self.history_index: int = len(self.history)
        self.prompt: str = DEFAULT_PROMPT
        self.cursor: str = DEFAULT_CURSOR
        self.debug: bool = False

    def _display(
        self, prompt: str, line: str, cursor_position: int, insert: bool
    ) -> None:
        click.echo(f"\r{' ' * (len(prompt) + len(line))}                \r", nl=False)
        click.echo(
            f"\nc: {cursor_position} l: {len(line)} cmd: {'yes' if line.startswith(':') else 'no'} {'I' if insert else ' '}               "
        )
        click.echo("\x1b[1A", nl=False)
        click.echo("\x1b[1A", nl=False)
        cursor = self.cursor
        text = line
        if line.startswith(":"):
            cursor = COMMAND_CURSOR
            text = line[1:]
        click.echo(f"\r{prompt}{cursor} {text}", nl=False)
        pos = cursor_position + len(prompt) + 2  # 2 for the cursor and space
        if line.startswith(":"):
            pos -= 1
        click.echo("\r", nl=False)  # go to the start of the line
        click.echo("\x1b[C" * pos, nl=False)

    def _safe_print(self, text: str) -> None:
        out = ""
        for c in text:
            if ord(c) < 32 or ord(c) > 126:
                out += f"\\x{ord(c):02x}"
            else:
                out += c
            out += " "
        click.echo(out)

    def __input(self, prompt: str, cursor: str = DEFAULT_CURSOR) -> str:
        self.cursor = cursor
        user_input = ""
        cursor_position = 0
        insert = True
        self._display(prompt, user_input, cursor_position, insert)
        while True:
            key = click.getchar()
            if key == "\r":  # Enter key
                if user_input:
                    if (
                        self.history_index == len(self.history)
                        or self.history[self.history_index] != user_input
                    ):
                        self.history.append(user_input)
                    click.echo("\n")
                break
            elif key == "\x7f":  # Backspace
                if cursor_position == 1 and user_input[0] == ":":  # Command mode
                    if len(user_input) == 1:
                        user_input = ""
                    else:
                        user_input = user_input[1:]
                    cursor_position = 0
                elif cursor_position > 0:
                    cursor_position -= 1
                    user_input = (
                        user_input[:cursor_position] + user_input[cursor_position + 1 :]
                    )
            elif key == "\x15":  # Ctrl+U (clear line)
                click.echo("\r" + " " * len(prompt) + "\r", nl=False)
                click.echo(f"{prompt}", nl=False)
                user_input = ""
                cursor_position = 0
            elif len(key) > 1 and key[0] == "\x1b":  # Arrow keys
                handled = True
                if len(key) == 3:
                    inp = key[2]
                    if inp == "A":  # Up arrow
                        history_index = max(self.history_index - 1, 0)
                        if history_index < len(self.history):
                            click.echo("\r" + " " * len(prompt) + "\r", nl=False)
                            user_input = self.history[history_index].strip()
                            if user_input.startswith(":"):
                                click.echo(f"{prompt}\b\b$ {user_input[1:]}", nl=False)
                            else:
                                click.echo(f"{prompt}{user_input}", nl=False)
                            cursor_position = len(user_input)
                    elif inp == "B":  # Down arrow
                        history_index = min(history_index + 1, len(self.history))
                        if history_index < len(self.history):
                            user_input = self.history[history_index].strip()
                            cursor_position = len(user_input)
                    elif inp == "C":  # Right arrow
                        if cursor_position >= len(user_input):
                            continue
                        cursor_position = min(cursor_position + 1, len(user_input))
                    elif inp == "D":  # Left arrow
                        if cursor_position <= 0:
                            continue
                        cursor_position = max(cursor_position - 1, 0)
                    elif inp == "H":  # Home
                        cursor_position = 0
                        if user_input.startswith(":"):
                            cursor_position = 1
                    elif inp == "F":  # End
                        cursor_position = len(user_input)
                    else:
                        handled = False
                elif len(key) == 4:  # Function keys
                    inp = key[1:]
                    if inp == "[2~":  # Insert key
                        insert = not insert
                        self._display(prompt, user_input, cursor_position, insert)
                    else:
                        handled = False
                if self.debug is False or handled is True:
                    continue
                print(f"\n\nUnhandled escape code (length {len(key)}):")
                self._safe_print(key)
                sys.exit(1)
            else:
                if len(key) > 1 or ord(key) < 32 or ord(key) > 126:
                    if self.debug is False:
                        continue
                    print(f"\n\nUnhandled command code (length {len(key)}):")
                    self._safe_print(key)
                    sys.exit(1)

                if cursor_position == len(user_input):
                    user_input += key
                else:
                    user_input = (
                        user_input[:cursor_position]
                        + key
                        + user_input[cursor_position:]
                    )
                cursor_position += 1
            self._display(prompt, user_input, cursor_position, insert)
        click.echo()
        return user_input

    def __load_history(self) -> list[str]:
        history: list[str] = []
        if pathlib.Path(self.__history_path).expanduser().exists():
            with open(pathlib.Path(self.__history_path).expanduser(), "r") as file:
                history = file.readlines()
            for line in history:
                line = line.strip()
        self.history_index = len(history)
        return history

    def __save_history(self) -> None:
        with open(pathlib.Path(self.__history_path).expanduser(), "w") as file:
            for line in self.history:
                file.write(line + "\n")
        # print("History saved, size: ", len(self.history))

    def __help(self) -> None:
        click.echo("Macal DSL Interpreter REPL")
        click.echo()
        click.echo(":clear - Clear the screen")
        click.echo(":clear_history - Clears the cli history")
        click.echo(":exit, :quit, :q, :x - Exit the REPL")
        click.echo(":help - Print this help message")
        click.echo(":print_ast - Print the AST Tree of the last executed 'program'")
        click.echo(":print_history - Print the CLI history")
        click.echo(
            ":print_tokens - Print the Lexer tokens of the last executed 'program'"
        )
        click.echo(":print_vars - Print the variables")
        click.echo(":reset - Reset the environment")
        click.echo()

    def __clear_history(self) -> None:
        self.history = []
        self.history_index = 0
        click.echo()
        click.echo("CLI history cleared.")
        click.echo()

    def __reset(self, env: Env, parser_state: ParserState) -> None:
        env.reset()
        parser_state.reset()
        click.echo()
        click.echo("Environment reset.")
        click.echo()

    def __print_ast(self, program: Optional[ProgramNode]) -> None:
        click.echo()
        if program is not None:
            click.echo(program.json(True))
        else:
            click.echo("No program to print.")
        click.echo()

    def __print_history(self) -> None:
        click.echo()
        for i, line in enumerate(self.history):
            click.echo(f"{i+1}: {line}")
        click.echo()

    def __print_tokens(self, tokens: Optional[list[Token]]) -> None:
        click.echo()
        if tokens is not None:
            for token in tokens:
                click.echo(token)
        else:
            click.echo("No tokens to print.")
        click.echo()

    def __print_vars(self, env: Env) -> None:
        click.echo()
        click.echo("Global Variables:")
        for k, v in env.variables.items():
            if (
                k
                in [  # ensure that the built in variables/native functions don't show up.
                    "true",
                    "false",
                    "nil",
                    "print",
                    "ms_timer",
                    "ns_timer",
                    "ShowVersion",
                ]
            ):
                continue
            click.echo(f"{k} = {v}")
        click.echo("---")
        click.echo()

    def __execute(
        self,
        command: str,
        parser: Parser,
        parser_state: ParserState,
        interpreter: Interpreter,
        debug: bool,
        env: Env,
    ) -> None:
        if command == "":
            return
        if not command.endswith(";"):
            command = f"{command};"
        program = parser.ProduceAST(source=command, debug=debug, state=parser_state)
        if program is not None:
            if debug:
                click.echo(program.json(True))
                click.echo()
            value = interpreter.evaluate(program, env)
            if value is not None:
                if value.type == ValueType.Halt:
                    if isinstance(value, HaltValue):
                        if value.exit_value is not None:
                            click.echo(
                                f"Program halted with exit value: {value.exit_value}"
                            )
                        else:
                            click.echo("Program halted.")
                elif value.type != ValueType.Nil:
                    click.echo()
                    click.echo(value)
                    click.echo()
        else:
            click.echo("No program to execute.")

    def run(self, args: argparse.Namespace) -> None:
        click.echo("Macal DSL Interpreter REPL")
        click.echo("Type ':exit' to exit, :help for help")
        self.debug = args.debug
        parser = Parser("repl")
        parser_state = ParserState(name="Global", parent=None, filename="repl")
        interpreter = Interpreter()
        env = Env.CreateGlobalEnv()
        current_dir = pathlib.Path(__file__).parent.absolute()
        interpreter.add_path(str(current_dir))
        tokens: Optional[list[Token]] = None
        program: Optional[ProgramNode] = None
        if args.lib:
            interpreter.add_path(str(pathlib.Path(args.lib).expanduser()))
        while True:
            text = self.__input(self.prompt, self.cursor)
            text = text.strip()
            if text.startswith(":"):
                if text == ":clear":
                    click.clear()
                elif text == ":clear_history":
                    self.__clear_history()
                elif text == ":exit" or text == ":quit" or text == ":q" or text == ":x":
                    break
                elif text == ":help":
                    self.__help()
                elif text == ":print_ast":
                    self.__print_ast(program)
                elif text == ":print_history":
                    self.__print_history()
                elif text == ":print_tokens":
                    self.__print_tokens(tokens)
                elif text == ":print_vars":
                    self.__print_vars(env)
                elif text == ":reset":
                    self.__reset(env, parser_state)
            else:
                print(f"Text: {text}")
                continue
                try:
                    self.__execute(
                        text,
                        parser,
                        parser_state,
                        interpreter,
                        args.debug,
                        env,
                    )
                    tokens = parser.tokens
                    program = parser.program

                except SyntaxError as e:
                    click.echo(f"{e}")
                except RuntimeError as e:
                    click.echo(f"{e}")
                except RuntimeErrorLC as e:
                    click.echo(f"{e}")
        self.__save_history()


def main() -> None:
    repl = MRepl()
    repl.run(parse_args())


if __name__ == "__main__":
    main()
