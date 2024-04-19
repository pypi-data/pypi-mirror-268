# -*- coding: utf-8 -*-
#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      2024-03-23
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


# System library for Macal DSL interpreter.
# This module contains the system functions and constants for the Macal interpreter.
#
# One of the advantages of the Macal DSL Library system is you can use normal Python functions.
#
# This is a hack for the Native functions.
#

from macal import __about__
import sys


def Print(*args) -> None:
    """Prints the arguments to the console."""
    print(
        "".join(str(arg).lower() if isinstance(arg, bool) else str(arg) for arg in args)
    )


def ShowVersion() -> None:
    """Prints the version of Macal."""
    print("Macal DSL Interpreter")
    print(f"Version:   {__about__.__version__}")
    print(f"Author:    {__about__.__author__}")
    print(f"Email:     {__about__.__email__}")
    print(f"License:   {__about__.__license__}")
    print(f"Copyright: {__about__.__copyright__}")
