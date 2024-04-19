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

# This module contains the runtime environment for the Macal interpreter.

from __future__ import annotations
from typing import Optional, Dict
from macal.runtime.values import (
    IRuntimeValue,
    BooleanValue,
    NilValue,
    NativeFunctionValue,
    ValueType,
)

from macal.runtime.native.time import ms_timer, ns_timer
from macal.runtime.native.system import Print, ShowVersion
from macal.runtime.mimporter import ModuleInfo, ModuleImport
from macal.mexceptions import RuntimeError, RuntimeErrorLC
from macal.frontend.ast.metadata import NodeMetadata
import json


class Env:
    def __init__(self, parent: Optional[Env], name: Optional[str] = "Local") -> None:
        self.name = "Global" if parent is None else name
        self.parent = parent
        self.variables: Dict[str, IRuntimeValue] = {}
        self.constants: list[str] = []
        self.is_in_loop = False
        self.is_in_function = False
        self.is_in_switch = False
        self.external_modules: Dict[str, ModuleInfo] = {}
        self.libraries: Dict[str, Env] = {}

    def reset(self) -> None:  # reset is used by repl to reset the environment
        self.variables = {}
        self.constants = []
        self.is_in_loop = False
        self.is_in_function = False
        self.is_in_switch = False
        self.external_modules = {}
        self.libraries = {}
        if self.parent is not None:
            self.parent.reset()

    def create_child_env(self, name: Optional[str] = "Local") -> Env:
        child = Env(self, name)
        child.is_in_function = self.is_in_function
        child.is_in_loop = self.is_in_loop
        self.is_in_switch = self.is_in_switch
        return child

    def get_global_env(self) -> Env:
        env = self
        while env.parent is not None:
            env = env.parent
        return env

    @staticmethod
    def CreateGlobalEnv() -> Env:
        env = Env(None)
        env.DeclareVar("true", BooleanValue(True), NodeMetadata.new(), True)
        env.DeclareVar("false", BooleanValue(False), NodeMetadata.new(), True)
        env.DeclareVar("nil", NilValue(), NodeMetadata.new(), True)
        env.DeclareVar(
            "ms_timer", NativeFunctionValue(ms_timer), NodeMetadata.new(), True
        )
        env.DeclareVar(
            "ns_timer", NativeFunctionValue(ns_timer), NodeMetadata.new(), True
        )
        env.DeclareVar("print", NativeFunctionValue(Print), NodeMetadata.new(), True)
        env.DeclareVar(
            "ShowVersion", NativeFunctionValue(ShowVersion), NodeMetadata.new(), True
        )
        return env

    def DeclareVar(
        self,
        name: str,
        value: IRuntimeValue,
        metadata: Optional[NodeMetadata] = None,
        is_constant: bool = False,
    ) -> IRuntimeValue:
        if is_constant:
            if name in self.constants:
                raise RuntimeError(f"Illegal assignment to constant '{name}'.")
            self.constants.append(name)
        self.variables[name] = value
        return value

    def AssignVar(
        self, name: str, value: IRuntimeValue, meta: Optional[NodeMetadata]
    ) -> IRuntimeValue:
        env: Optional[Env] = self.Resolve(name)
        if env is not None and name in env.constants:
            msg = f"Illegal assignment to constant '{name}'"
            if meta is not None:
                raise RuntimeErrorLC(msg, meta)
            raise RuntimeError(msg)
        if env is None:
            env = self
        env.variables[name] = value
        return value

    def _set_const(self, name: str, value: IRuntimeValue) -> None:
        """This method is only used by the evaluator of the foreach statement to set the it iterator value."""
        env: Optional[Env] = self.Resolve(name)
        if env is None:
            env = self
        env.variables[name] = value

    def _set_var(self, name: str, value: IRuntimeValue) -> None:
        self.variables[name] = value

    def Resolve(self, name: str) -> Optional[Env]:
        if name in self.variables:
            return self
        if self.parent is None:
            return None
        return self.parent.Resolve(name)

    def ResolveLibrary(self, name: str) -> Optional[Env]:
        env = self.get_global_env()
        for lib in env.libraries.values():
            if name in lib.variables:
                return lib
        return None

    def LookupVar(
        self, name: str, meta: Optional[NodeMetadata], _allow_not_found: bool = False
    ) -> IRuntimeValue:
        env = self.Resolve(name)
        if env is None:
            env = self.ResolveLibrary(name)
        if env is None:
            if _allow_not_found is True:
                return NilValue()
            msg = f"Variable '{name}' not found"
            if meta is not None:
                raise RuntimeErrorLC(msg, meta)
            raise RuntimeError(msg)
        var = env.variables.get(name)
        if var is None:
            if (
                _allow_not_found
            ):  # this is used by the evaluator of the import statement, because i want to throw another error message.
                return NilValue()
            msg = f"Variable '{name}' not found"
            if meta is not None:
                raise RuntimeErrorLC(msg, meta)
            raise RuntimeError(msg)
        if (
            var.type not in [ValueType.Function, ValueType.NativeFunction]
            and self.variables.get(name, None) is None
        ):
            if self.is_in_function:
                msg = f"Variable '{name}' not found in function scope"
                if meta is not None:
                    raise RuntimeErrorLC(msg, meta)
                raise RuntimeError(msg)
        return var

    def FindVar(self, name: str) -> Optional[IRuntimeValue]:
        env = self.Resolve(name)
        if env is None:
            env = self.ResolveLibrary(name)
        if env is None:
            return None
        return env.variables.get(name)

    def LookupModule(self, name: str) -> Optional[ModuleInfo]:
        env = self.get_global_env()
        if name in env.external_modules:
            return env.external_modules[name]
        return None

    def ImportModule(self, name: str, paths: list[str]) -> bool:
        module = self.LookupModule(name)
        if module is not None:
            return True
        importer = ModuleImport(paths)
        module = importer.load_module(name)
        if module is None:
            return False
        global_env = self.get_global_env()
        global_env.external_modules[name] = module
        return True

    def json(self) -> dict:
        return {
            "name": self.name,
            "variables": {k: f"{v}" for k, v in self.variables.items()},
            "constants": self.constants,
            "is_in_loop": self.is_in_loop,
            "is_in_function": self.is_in_function,
            "is_in_switch": self.is_in_switch,
            "external_modules": {
                name: module.json() for name, module in self.external_modules.items()
            },
            "libraries": {name: env.json() for name, env in self.libraries.items()},
        }

    def print(self) -> None:
        env = self.get_global_env()
        if env is not None:
            print(json.dumps(env.json(), indent=4))

    def __evaluate__(self, varname) -> bool:
        print()
        print(f"Evaluating environment for: '{varname}' in '{self.name}' environment")
        for k, _ in self.variables.items():
            # print(f"{k} == {varname} -> {k == varname}")
            if k == varname:
                print(f"Variable '{k}' found in '{self.name}' environment")
                return True
        print(
            f"Variable '{varname}' not found in '{self.name}' environment, trying parent environment"
        )
        if self.parent is not None:
            r = self.parent.__evaluate__(varname)
            if r is True:
                return True
        print(f"Variable '{varname}' not found.")
        return False
