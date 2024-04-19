# -*- coding: utf-8 -*-
#
# Product:   Macal
# Author:    Marco Caspers
# Email:     SamaDevTeam@westcon.com
# License:   MIT License
# Date:      2024-03-24
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

# This module contains the Python module information object for the Macal interpreter.


from typing import Any, Optional
from pathlib import Path
from inspect import getmembers, isfunction
import importlib
import importlib.util
import os


class ModuleInfo:
    def __init__(self, name: str, module: Any) -> None:
        self.name = name
        self.module = module
        members = getmembers(module)
        self._object_dict = {name: obj for name, obj in members}
        self.functions = {
            name: obj for name, obj in self._object_dict.items() if isfunction(obj)
        }

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return self.__str__()

    def json(self) -> dict:
        return {
            "name": self.name,
            "functions": [name for name in self.functions.keys()],
            "object_dict": {
                name: f"{type(obj)}" for name, obj in self._object_dict.items()
            },
        }


class ModuleImport:
    def __init__(self, paths: list[str]) -> None:
        self.paths: list[str] = paths
        self.module: Optional[Any] = None
        self.module_info: Optional[ModuleInfo] = None

    def _import_module(self, name: str) -> bool:
        try:
            self.module = importlib.import_module(name)
            self.module_info = ModuleInfo(name, self.module)
            return True
        except ModuleNotFoundError:
            return False

    def _import_module_from_path(self, name: str) -> bool:
        for path in self.paths:
            try:
                path = os.path.join(path, f"{name}.py")
                if not os.path.exists(path):
                    continue
                spec = importlib.util.spec_from_file_location(name, path)
                if spec is None:
                    continue
                self.module = importlib.util.module_from_spec(spec)
                if spec.loader is None:
                    continue
                spec.loader.exec_module(self.module)
                self.module_info = ModuleInfo(name, self.module)
                return True
            except ModuleNotFoundError as e:
                print("@ Module not found: ", e)
                continue
            except FileNotFoundError as e:
                print("@ File not found: ", e)
                continue
            except ImportError as e:
                print("@ Import error: ", e)
                continue
        return False

    def load_module(self, name: str) -> Optional[ModuleInfo]:
        if self._import_module(name):
            return self.module_info
        if self._import_module_from_path(name):
            return self.module_info
        return None
