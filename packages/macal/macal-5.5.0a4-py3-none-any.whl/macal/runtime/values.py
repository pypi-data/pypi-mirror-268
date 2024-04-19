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

# This module contains the runtime values for the Macal interpreter.


from __future__ import annotations
from typing import Protocol, Callable, runtime_checkable, Any, Optional, Union
from enum import Enum, auto
from macal.frontend.ast.node import IStmt
from macal.frontend.ast.metadata import NodeMetadata
from macal.mexceptions import RuntimeErrorLC

from macal.runtime.value_type import ValueType
import sys


class ObjectType(Enum):
    Object = auto()
    Array = auto()
    Record = auto()


@runtime_checkable
class IRuntimeValue(Protocol):
    @property
    def type(self) -> ValueType: ...
    @property
    def iterable(self) -> bool: ...
    @property
    def value(self) -> Any: ...
    def __str__(self) -> str: ...
    def json(self) -> dict: ...


@runtime_checkable
class IIterable(Protocol):
    def Next(self) -> IRuntimeValue: ...
    def Reset(self) -> None: ...


class NilValue(IRuntimeValue):
    def __init__(self) -> None:
        self._type: ValueType = ValueType.Nil
        self._value: str = "nil"
        self._iterabe: bool = False

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def value(self) -> str:
        return self._value

    def __str__(self) -> str:
        return "nil"

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "value": self.value,
        }


class DefaultValue(IRuntimeValue):
    def __init__(self) -> None:
        self._type: ValueType = ValueType.Default
        self._value: str = "default"
        self._iterabe: bool = False

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def value(self) -> str:
        return self._value

    def __str__(self) -> str:
        return "default"

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "value": self.value,
        }


class IntegerValue(IRuntimeValue):
    def __init__(self, value: int) -> None:
        self._type: ValueType = ValueType.Integer
        self._value: int = value
        self._iterabe: bool = False

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def value(self) -> int:
        return self._value

    def __str__(self) -> str:
        return str(self._value)

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "value": self.value,
        }


class FloatValue(IRuntimeValue):
    def __init__(self, value: float) -> None:
        self._type: ValueType = ValueType.Float
        self._value: float = value
        self._iterabe: bool = False

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def value(self) -> float:
        return self._value

    def __str__(self) -> str:
        return str(self._value)

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "value": self.value,
        }


class StringValue(IRuntimeValue, IIterable):
    def __init__(
        self,
        value: str,
        meta: NodeMetadata,
        literal: bool = False,
    ) -> None:
        self._type: ValueType = ValueType.String
        self._literal: bool = literal
        self._value: str = self.handle_escapes(value)
        self._iterabe: bool = True
        self._index: int = -1
        self._meta: NodeMetadata = meta
        self.index: Optional[int] = None

    def handle_escapes(self, string: str) -> str:
        if self.literal:
            return string
        s = string.replace("\\n", "\n")
        s = s.replace("\\t", "\t")
        s = s.replace("\\r", "\r")
        s = s.replace("\\b", "\b")
        s = s.replace("\\0", "\0")
        s = s.replace("{{", "{")
        s = s.replace("}}", "}")
        return s

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def length(self) -> int:
        return len(self.value)

    @property
    def value(self) -> str:
        return self._value

    @property
    def literal(self) -> bool:
        return self._literal

    def __str__(self) -> str:
        return self._value

    def Next(self) -> IRuntimeValue:
        meta = self._meta
        if self._index < self.length - 1:
            self._index += 1
            meta.column += self._index
            return StringValue(self._value[self._index], meta)
        else:
            return NilValue()

    def get(self, index: int, meta: NodeMetadata) -> IRuntimeValue:
        if index < 0 or index >= self.length:
            raise RuntimeErrorLC(f"E: Index out of bounds {index}", meta)
        return StringValue(self._value[index], meta)

    def set(self, value: str) -> None:
        if not isinstance(value, str):
            raise RuntimeError(f"Invalid string value: {value}")
        self._value = value

    def Reset(self) -> None:
        self._index = -1

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "value": self.value,
            "length": self.length,
            "iterable": self.iterable,
            "index": self._index,
            "metadata": self._meta.json(),
        }


class BooleanValue(IRuntimeValue):
    def __init__(self, value: bool, metadata: Optional[NodeMetadata] = None) -> None:
        self._type: ValueType = ValueType.Boolean
        self._value: bool = value
        self._iterabe: bool = False
        self._metadata: Optional[NodeMetadata] = metadata

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def value(self) -> bool:
        return self._value

    def __str__(self) -> str:
        return "true" if self._value else "false"

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "value": self.value,
            "metadata": self._metadata.json() if self._metadata else None,
        }


class ReturnValue(IRuntimeValue):
    def __init__(self, value: IRuntimeValue) -> None:
        self._type: ValueType = ValueType.Return
        self._value: IRuntimeValue = value
        self._iterabe: bool = False

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def value(self) -> IRuntimeValue:
        return self._value

    def __str__(self) -> str:
        return str(self._value)

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "value": self.value,
        }


class HaltValue(IRuntimeValue):
    def __init__(self, value: IRuntimeValue) -> None:
        self._type: ValueType = ValueType.Halt
        self._value: IRuntimeValue = value
        self._iterabe: bool = False

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def value(self) -> IRuntimeValue:
        return self._value

    @property
    def exit_value(self) -> IRuntimeValue:
        return self._value

    def __str__(self) -> str:
        return "halt"

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "value": self.value,
        }


class BreakValue(IRuntimeValue):
    def __init__(self) -> None:
        self._type: ValueType = ValueType.Break
        self._iterabe: bool = False

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def value(self) -> BreakValue:
        return self

    def __str__(self) -> str:
        return "break"

    def json(self) -> dict:
        return {
            "type": self.type.name,
        }


class ContinueValue(IRuntimeValue):
    def __init__(self) -> None:
        self._type: ValueType = ValueType.Continue
        self._iterabe: bool = False

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def value(self) -> ContinueValue:
        return self

    def __str__(self) -> str:
        return "continue"

    def json(self) -> dict:
        return {
            "type": self.type.name,
        }


class ObjectValue(IRuntimeValue, IIterable):
    def __init__(
        self,
        properties: dict[str, IRuntimeValue],
        metadata: Optional[NodeMetadata] = None,
    ) -> None:
        self._type: ValueType = ValueType.Object
        self._otype: ObjectType = ObjectType.Object
        self._properties: dict[str, IRuntimeValue] = properties
        self._iterabe: bool = True
        self._iterator: int = -1
        self.object_index: Optional[Union[str, int]] = None
        self.metadata: Optional[NodeMetadata] = metadata

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def otype(self) -> ObjectType:
        return self._otype

    @otype.setter
    def otype(self, value: ObjectType) -> None:
        self._otype = value

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def properties(self) -> dict[str, IRuntimeValue]:
        return self._properties

    @property
    def keys(self) -> list[str]:
        return list(self._properties.keys())

    @property
    def length(self) -> int:
        return len(self._properties.keys())

    @property
    def value(self) -> dict[str, IRuntimeValue]:
        return self._properties

    def __str__(self) -> str:
        return "object"

    def Next(self) -> IRuntimeValue:
        if self._iterator < self.length - 1:
            self._iterator += 1
            return self._properties[self.keys[self._iterator]]
        else:
            return NilValue()

    def Reset(self) -> None:
        self._iterator = -1

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "otype": self.otype.name,
            "properties": {key: value.json() for key, value in self.properties.items()},
            "length": self.length,
            "iterable": self.iterable,
            "iterator": self._iterator,
            "index": self.object_index,
            "metadata": self.metadata.json() if self.metadata else None,
        }


class ArrayObject(ObjectValue):
    def __init__(self, meta: NodeMetadata) -> None:
        super().__init__({}, meta)
        self._otype = ObjectType.Array
        self._metadata = meta
        self.object_index: Optional[int] = None
        self.new_index: bool = False

    @property
    def elements(self) -> list[IRuntimeValue]:
        return list(self._properties.values())

    def append(self, value: IRuntimeValue) -> None:
        self._properties[str(self.length)] = value

    def get(self, index: int, meta: NodeMetadata) -> IRuntimeValue:
        if index < 0 or index >= self.length:
            raise RuntimeErrorLC(f"Array index out of bounds {index}", meta)
        self.index = index
        return self.elements[index]

    def set(self, index: int, value: IRuntimeValue, meta: NodeMetadata) -> None:
        if index < 0 or index >= self.length:
            raise RuntimeErrorLC(f"Array index out of bounds {index}", meta)
        self._properties[str(index)] = value

    def clear(self) -> None:
        self._properties = {}

    def Next(self) -> IRuntimeValue:
        if self._iterator < self.length - 1:
            self._iterator += 1
            return self.elements[self._iterator]
        else:
            return NilValue()

    def copy(self) -> ArrayObject:
        result = ArrayObject(self._metadata)
        for el in self.elements:
            result.append(el)  # type: ignore
        return result

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "otype": self.otype.name,
            "elements": [el.json() for el in self.elements],
            "length": self.length,
            "iterable": self.iterable,
            "iterator": self._iterator,
            "index": self.object_index,
            "metadata": self._metadata.json(),
        }


class RecordObject(ObjectValue):
    def __init__(self, meta: NodeMetadata) -> None:
        super().__init__({}, meta)
        self._otype = ObjectType.Record
        self._metadata = meta
        self.object_index: Optional[str] = None

    @property
    def fields(self) -> dict[str, IRuntimeValue]:
        return self._properties

    @property
    def columns(self) -> list[str]:
        return list(self._properties.keys())

    def Next(self) -> IRuntimeValue:
        if self._iterator < self.length - 1:
            self._iterator += 1
            return StringValue(self.keys[self._iterator], meta=self.metadata)  # type: ignore
        else:
            return NilValue()

    def get(self, index: str, meta: NodeMetadata, default: Any = None) -> IRuntimeValue:
        self.index = index
        if not self.index in self.columns:
            if default is None:
                raise RuntimeErrorLC(f"Record invalid key {index}", meta)
            return default
        return self.fields[index]

    def clear(self) -> None:
        self._properties = {}

    def copy(self) -> RecordObject:
        result = RecordObject(self._metadata)
        for key, value in self.fields.items():
            result.fields[key] = value.copy()  # type: ignore
        return result

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "otype": self.otype.name,
            "columns": self.columns,
            "fields": {key: value.json() for key, value in self.fields.items()},
            "length": self.length,
            "iterable": self.iterable,
            "iterator": self._iterator,
            "index": self.object_index,
            "metadata": self._metadata.json(),
        }


class NativeFunctionValue(IRuntimeValue):
    def __init__(self, call: Callable) -> None:
        self._type: ValueType = ValueType.NativeFunction
        self._call: Callable = call
        self._iterabe: bool = False

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def callback(self) -> Callable:
        return self._call

    @property
    def value(self) -> NativeFunctionValue:
        return self

    def __str__(self) -> str:
        return "native function"

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "callback": self.callback,
        }


class FunctionValue(IRuntimeValue):
    def __init__(
        self, name: str, params: list[str], env: Any, body: list[IStmt]
    ) -> None:
        self._type: ValueType = ValueType.Function
        self._name: str = name
        self._params: list[str] = params
        self._env = env
        self.body: list[IStmt] = body
        self._iterabe: bool = False

    @property
    def type(self) -> ValueType:
        return self._type

    @property
    def iterable(self) -> bool:
        return self._iterabe

    @property
    def env(self):
        return self._env

    @property
    def name(self) -> str:
        return self._name

    @property
    def params(self) -> list[str]:
        return self._params

    @property
    def value(self) -> FunctionValue:
        return self

    def __str__(self) -> str:
        return "function"

    def json(self) -> dict:
        return {
            "type": self.type.name,
            "name": self.name,
            "params": self.params,
            "env": self.env,
            "body": [str(stmt) for stmt in self.body],
        }
