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

# This module contains the main Macal DSL Interpreter.

from __future__ import annotations
from typing import Optional, Dict, Any, Union, Coroutine

# region Value Types
from macal.runtime.values import (
    IRuntimeValue,
    IIterable,
    IntegerValue,
    FloatValue,
    StringValue,
    BooleanValue,
    NilValue,
    ObjectValue,
    FunctionValue,
    ValueType,
    NativeFunctionValue,
    ReturnValue,
    HaltValue,
    BreakValue,
    ContinueValue,
    ArrayObject,
    RecordObject,
    DefaultValue,
)

# endregion

from macal.frontend.ast.kind import NodeKind, ObjectKind

# region AST nodes
from macal.frontend.ast.node import (
    # Literals
    ProgramNode,
    IntLiteral,
    FloatLiteral,
    StringLiteral,
    Identifier,
    ObjectLiteral,
    LibraryLiteral,
    ArrayLiteral,
    RecordLiteral,
    # Statements
    IStmt,
    VarDeclaration,
    FunctionDeclaration,
    IfStatement,
    ElifStatement,
    ElseStatement,
    ReturnStatement,
    BreakStatement,
    ContinueStatement,
    HaltStatement,
    WhileStatement,
    ForEachStatement,
    SwitchStatement,
    CaseStatement,
    DefaultCaseStatement,
    IncludeStatement,
    TypeStatement,
    IsTypeStatement,
    SelectStatement,
    SelectField,
    # Expressions
    IExpr,
    AssignmentExpr,
    BinaryExpr,
    UnaryExpr,
    CallExpr,
    MemberExpr,
)

# endregion

from macal.runtime.menvironment import Env
from macal.frontend.mparser import Parser
from macal.__about__ import __version__
from macal.mexceptions import RuntimeError, RuntimeErrorLC
from macal.frontend.ast.metadata import NodeMetadata
import os
import sys
import json

DEFAULT_LIBRARY_PATH = "library"
DEFAULT_SOURCE_FILE_EXTENSION = ".mcl"
DEFAULT_BINARY_FILE_EXTENSION = ".mcb"


# Interpreter class
class Interpreter:
    def __init__(self) -> None:
        self.search_paths: list[str] = [
            # os.path.join(os.path.dirname(__file__), DEFAULT_LIBRARY_PATH),
        ]
        self.search_paths.append(os.getcwd())
        self.interpreter_state: str = "init"

    def add_path(self, path: str) -> None:
        if path not in self.search_paths:
            self.search_paths.append(path)

    def _eval_numeric_binary_expr(
        self, lhs: IRuntimeValue, rhs: IRuntimeValue, op: str
    ) -> IRuntimeValue:
        if op == "+.":
            return StringValue(f"{str(lhs.value)}{str(rhs.value)}", NodeMetadata.new())
        # Convert integer to float if necessary
        if isinstance(lhs, IntegerValue) and isinstance(rhs, FloatValue):
            lhs = FloatValue(float(lhs.value))
        if isinstance(lhs, FloatValue) and isinstance(rhs, IntegerValue):
            rhs = FloatValue(float(rhs.value))
        if isinstance(lhs, IntegerValue) and isinstance(rhs, IntegerValue):
            if op == "+":
                return IntegerValue(lhs.value + rhs.value)
            elif op == "-":
                return IntegerValue(lhs.value - rhs.value)
            elif op == "*":
                return IntegerValue(lhs.value * rhs.value)
            elif op == "/":
                if rhs.value == 0:
                    raise RuntimeError("Division by zero.")
                rv = lhs.value / rhs.value
                if isinstance(rv, int):
                    return IntegerValue(rv)
                return FloatValue(rv)
            elif op == "%":
                return IntegerValue(lhs.value % rhs.value)
            elif op == "^":
                return IntegerValue(lhs.value**rhs.value)
            elif op == "<":
                return BooleanValue(lhs.value < rhs.value)
            elif op == ">":
                return BooleanValue(lhs.value > rhs.value)
            elif op == "<=":
                return BooleanValue(lhs.value <= rhs.value)
            elif op == ">=":
                return BooleanValue(lhs.value >= rhs.value)
            elif op == "==":
                return BooleanValue(lhs.value == rhs.value)
            elif op == "!=":
                return BooleanValue(lhs.value != rhs.value)
            elif op == "&&" or op == "and" or op == "&":
                return IntegerValue(lhs.value and rhs.value)
            elif op == "||" or op == "or" or op == "|":
                return IntegerValue(lhs.value and rhs.value)
            elif op == "xor":
                return IntegerValue(lhs.value and rhs.value)
            else:
                raise RuntimeError(f"Unknown operator '{op}' for integer values.")
        elif isinstance(lhs, FloatValue) and isinstance(rhs, FloatValue):
            if op == "+":
                return FloatValue(lhs.value + rhs.value)
            elif op == "-":
                return FloatValue(lhs.value - rhs.value)
            elif op == "*":
                return FloatValue(lhs.value * rhs.value)
            elif op == "/":
                if rhs.value == 0.0:
                    raise RuntimeError("Division by zero.")
                return FloatValue(lhs.value / rhs.value)
            elif op == "%":
                return FloatValue(lhs.value % rhs.value)
            elif op == "^":
                return FloatValue(lhs.value**rhs.value)
            elif op == "<":
                return BooleanValue(lhs.value < rhs.value)
            elif op == ">":
                return BooleanValue(lhs.value > rhs.value)
            elif op == "<=":
                return BooleanValue(lhs.value <= rhs.value)
            elif op == ">=":
                return BooleanValue(lhs.value >= rhs.value)
            elif op == "==":
                return BooleanValue(lhs.value == rhs.value)
            elif op == "!=":
                return BooleanValue(lhs.value != rhs.value)
            elif op == "&&" or op == "and" or op == "&":
                return FloatValue(lhs.value and rhs.value)
            elif op == "||" or op == "or" or op == "|":
                return FloatValue(lhs.value and rhs.value)
            elif op == "xor":
                return FloatValue(lhs.value and rhs.value)
            else:
                raise RuntimeError(f"Unknown operator '{op}' for float values.")
        elif (
            isinstance(lhs, IntegerValue)
            and isinstance(rhs, BooleanValue)
            and op == "=="
            or op == "!="
        ):
            if rhs.value is False and op == "==":
                return BooleanValue(rhs.value)
            else:
                return BooleanValue(not rhs.value)
        else:
            raise RuntimeError(
                f"Unsupported binary operation '{op}' for values of type '{lhs.type}' and '{rhs.type}'."
            )

    def _eval_boolean_binary_expr(
        self, lhs: IRuntimeValue, rhs: IRuntimeValue, op: str
    ) -> IRuntimeValue:
        if op == "+.":
            vl = lhs.value
            vr = rhs.value
            if isinstance(vl, bool):
                vl = "true" if vl else "false"
            else:
                vl = str(vl)
            if isinstance(vr, bool):
                vr = "true" if vr else "false"
            else:
                vr = str(vr)
            return StringValue(f"{vl}{vr}", NodeMetadata.new())
        if op == "and" or op == "&&" or op == "&":
            return BooleanValue(lhs.value and rhs.value)
        elif op == "or" or op == "||" or op == "|":
            return BooleanValue(lhs.value or rhs.value)
        elif op == "xor":
            return BooleanValue(lhs.value != rhs.value)
        elif op == "==":
            return BooleanValue(lhs.value == rhs.value)
        elif op == "!=":
            return BooleanValue(lhs.value != rhs.value)
        else:
            raise RuntimeError(f"Unknown operator '{op}' for boolean values.")

    def _eval_string_binary_expr(
        self, lhs: IRuntimeValue, rhs: IRuntimeValue, op: str
    ) -> IRuntimeValue:
        if op == "+":
            return StringValue(
                f"{lhs.value}{rhs.value}", NodeMetadata.new()
            )  # this should not be possible,
        # in principle the parser should catch that and return a syntax error.
        if op == "+.":  # This is the way to append strings to something else in Macal.
            return StringValue(f"{lhs.value}{rhs.value}", NodeMetadata.new())
        elif op == "<":
            return BooleanValue(lhs.value < rhs.value)
        elif op == ">":
            return BooleanValue(lhs.value > rhs.value)
        elif op == "<=":
            return BooleanValue(lhs.value <= rhs.value)
        elif op == ">=":
            return BooleanValue(lhs.value >= rhs.value)
        elif op == "==":
            return BooleanValue(lhs.value == rhs.value)
        elif op == "!=":
            return BooleanValue(lhs.value != rhs.value)
        else:
            raise RuntimeError(f"Unknown operator '{op}' for string values.")

    def _eval_nil_binary_expr(
        self, lhs: IRuntimeValue, rhs: IRuntimeValue, op: str
    ) -> IRuntimeValue:
        if op == "==":
            return BooleanValue(lhs.value == rhs.value)
        elif op == "!=":
            return BooleanValue(lhs.value != rhs.value)
        elif (
            op == "+."
        ):  # This is the way to append strings to something else in Macal.
            return StringValue(f"{lhs.value}{rhs.value}", NodeMetadata.new())
        return NilValue()

    def _eval_binary_expr(
        self,
        lhs: IRuntimeValue,
        rhs: IRuntimeValue,
        op: str,
    ) -> IRuntimeValue:
        if isinstance(lhs, NilValue) or isinstance(rhs, NilValue):
            return self._eval_nil_binary_expr(lhs, rhs, op)
        elif isinstance(lhs, IntegerValue) or isinstance(lhs, FloatValue):
            return self._eval_numeric_binary_expr(lhs, rhs, op)
        elif isinstance(lhs, BooleanValue):
            return self._eval_boolean_binary_expr(lhs, rhs, op)
        elif isinstance(lhs, StringValue):
            return self._eval_string_binary_expr(lhs, rhs, op)
        elif isinstance(rhs, BooleanValue) and op == "!=" or op == "==":
            if rhs.value is False and op == "==":
                return BooleanValue(not lhs.value)
            else:
                return BooleanValue(not (not lhs.value))
        else:
            raise RuntimeError(
                f"Unsupported binary operation '{op}' for value of type '{lhs.type}'."
            )

    def _eval_binary(self, expr: BinaryExpr, env: Env) -> IRuntimeValue:
        lhs = self.evaluate(expr.left, env)
        if expr.operator in ["&&", "and", "&"] and lhs.value is False:
            return BooleanValue(False)
        if expr.operator in ["||", "or", "|"] and lhs.value is True:
            return BooleanValue(True)
        rhs = self.evaluate(expr.right, env)
        return self._eval_binary_expr(lhs, rhs, expr.operator)

    def _eval_unary(self, expr: UnaryExpr, env: Env) -> IRuntimeValue:
        rhs = self.evaluate(expr.right, env)
        if expr.operator == "-":
            if isinstance(rhs, IntegerValue):
                return IntegerValue(-rhs.value)
            if isinstance(rhs, FloatValue):
                return FloatValue(-rhs.value)
        if expr.operator == "!" or expr.operator == "not":
            if isinstance(rhs, BooleanValue):
                return BooleanValue(not rhs.value)
            if isinstance(rhs, NilValue):
                return BooleanValue(True)
        if expr.operator == "++":
            if isinstance(rhs, IntegerValue):
                return IntegerValue(rhs.value + 1)
            if isinstance(rhs, FloatValue):
                return FloatValue(rhs.value + 1)
        if expr.operator == "--":
            if isinstance(rhs, IntegerValue) and isinstance(expr.right, Identifier):
                value = IntegerValue(rhs.value - 1)
                env.AssignVar(expr.right.name, value, expr.right.metadata)
                return value
            if isinstance(rhs, FloatValue) and isinstance(expr.right, Identifier):
                fvalue = FloatValue(rhs.value - 1)
                env.AssignVar(expr.right.name, fvalue, expr.right.metadata)
                return fvalue
        raise RuntimeErrorLC(
            f"Invalid unary expression {expr.operator} {expr.right}", expr.metadata
        )

    def _eval_identifier(self, expr: Identifier, env: Env) -> IRuntimeValue:
        if expr is None or expr.name is None:
            raise RuntimeErrorLC("Invalid nil identifier.", expr.metadata)
        return env.LookupVar(expr.name, expr.metadata)

    def _eval_var_assign(
        self, node: AssignmentExpr, varname: Identifier, env: Env
    ) -> IRuntimeValue:
        name = varname.name
        if node.operator == "=":
            return env.AssignVar(name, self.evaluate(node.value, env), node.metadata)
        op = node.operator
        if not op in ["+=", "-=", "*=", "/=", "%=", "^=", ".="]:
            raise RuntimeErrorLC(f"Invalid assignment operator '{op}'", node.metadata)
        lhs = env.LookupVar(name, varname.metadata)
        if not isinstance(lhs, StringValue) and op == ".=":
            raise RuntimeErrorLC(
                f"Invalid operator '{op}' for non-string variable", node.metadata
            )
        rhs = self.evaluate(node.value, env)
        return env.AssignVar(
            name, self._eval_binary_expr(lhs, rhs, op[0]), varname.metadata
        )

    def _eval_member_literal_array(
        self,
        var: ArrayObject,
        property: IExpr,
        assign: bool,
        depth: int,
        metadata: NodeMetadata,
        env: Env,
    ) -> IRuntimeValue:
        if isinstance(property, Identifier) and property.name == "[]":
            if assign:
                return var
            raise RuntimeErrorLC(f"Invalid array index '{property.name}'", metadata)
        index = self.evaluate(property, env).value  # type: ignore
        if not isinstance(index, int):
            raise RuntimeErrorLC(f"Invalid array index type '{index}'", metadata)
        if index < 0 or index >= var.length:
            raise RuntimeErrorLC(f"Array index out of bounds '{index}'", metadata)
        var.object_index = index
        if assign and depth == 0:
            return var
        return var.get(index, metadata)

    def _eval_member_literal_object(
        self,
        var: ObjectValue,
        property: IExpr,
        assign: bool,
        depth: int,
        metadata: NodeMetadata,
        env: Env,
    ) -> IRuntimeValue:
        index = self.evaluate(property, env).value  # type: ignore
        var.object_index = index
        if assign and depth == 0:
            return var
        vidxv = var.properties.get(index, NilValue())  # type: ignore
        if vidxv is not None and not isinstance(vidxv, NilValue):
            return vidxv
        raise RuntimeErrorLC(f"Record index '{index}' not found", metadata)

    def _eval_member_literal_record(
        self,
        var: RecordObject,
        property: IExpr,
        assign: bool,
        depth: int,
        metadata: NodeMetadata,
        env: Env,
    ) -> IRuntimeValue:
        index = self.evaluate(property, env).value
        if not isinstance(index, str):
            raise RuntimeErrorLC(f"Invalid record column type '{index}'", metadata)
        var.object_index = index
        if assign and depth == 0:
            return var
        vidxv = var.get(index, metadata, default=DefaultValue())  # type: ignore
        if isinstance(vidxv, DefaultValue):
            raise RuntimeErrorLC(f"Record column '{index}' not found", metadata)
        return vidxv

    def _eval_member_literal_string(
        self,
        var: StringValue,
        property: IExpr,
        assign: bool,
        depth: int,
        metadata: NodeMetadata,
        env: Env,
    ) -> IRuntimeValue:
        index = self.evaluate(property, env).value
        if not isinstance(index, int):
            raise RuntimeErrorLC(f"Invalid string index type '{index}'", metadata)
        if index < 0 or index >= len(var.value):
            raise RuntimeErrorLC(f"String index out of bounds '{index}'", metadata)
        var.index = index
        if assign and depth == 0:
            return var
        return StringValue(var.value[index], metadata)

    def _eval_member_literal(
        self, name: Identifier, member: MemberExpr, assign: bool, depth: int, env: Env
    ) -> IRuntimeValue:
        varname: str = name.name
        var = env.LookupVar(varname, name.metadata)
        if var is None:
            raise RuntimeErrorLC(f"Variable '{varname}' not found.", name.metadata)

        if isinstance(var, ArrayObject):
            return self._eval_member_literal_array(
                var=var,
                property=member.property,
                assign=assign,
                depth=depth,
                metadata=member.metadata,
                env=env,
            )
        if isinstance(var, RecordObject):
            return self._eval_member_literal_record(
                var=var,
                property=member.property,
                assign=assign,
                depth=depth,
                metadata=member.metadata,
                env=env,
            )
        if isinstance(var, ObjectValue):
            return self._eval_member_literal_object(
                var=var,
                property=member.property,
                assign=assign,
                depth=depth,
                metadata=member.metadata,
                env=env,
            )
        if isinstance(var, StringValue):
            return self._eval_member_literal_string(
                var=var,
                property=member.property,
                assign=assign,
                depth=depth,
                metadata=member.metadata,
                env=env,
            )
        raise RuntimeErrorLC(
            f"Invalid member expression {member.property}", member.metadata
        )

    def _eval_member_properties(
        self, name: Identifier, member: MemberExpr, assign: bool, depth: int, env: Env
    ):
        varname: str = name.name
        var = env.LookupVar(varname, name.metadata)
        if isinstance(var, ArrayObject):
            raise RuntimeErrorLC(f"Invalid property on array", member.metadata)
        if not isinstance(member.property, Identifier):
            raise RuntimeErrorLC(
                f"Invalid property type ({member.property.kind.name})", member.metadata
            )
        if isinstance(var, ObjectValue):
            if assign is True and depth == 0:
                var.object_index = member.property.name
                return var
            return var.properties.get(member.property.name, NilValue())
        if isinstance(var, RecordObject):
            if assign is True and depth == 0:
                var.object_index = member.property.name
                return var
            return var.get(member.property.name, member.metadata, NilValue())

    def _walk_reverse(self, member: IExpr, env: Env) -> IRuntimeValue:
        if not isinstance(member, MemberExpr):
            raise RuntimeErrorLC(f"Invalid member expression {member}", member.metadata)
        if isinstance(member.object, Identifier):
            var = env.LookupVar(member.object.name, member.object.metadata)
            if member.computed is True:
                index = self.evaluate(member.property, env)
            else:
                index = self._eval_member_property(member, env)
            if isinstance(var, NilValue):
                return var
            if isinstance(var, ArrayObject):
                if not isinstance(index.value, int):
                    raise RuntimeErrorLC(
                        f"Invalid array index type '{index.value}'", member.metadata
                    )
                return var.get(index.value, member.metadata)
            if isinstance(var, RecordObject):
                return var.get(index.value, member.metadata, NilValue())
            if isinstance(var, ObjectValue):
                return var.properties.get(index.value, NilValue())
            if isinstance(var, StringValue):
                return var.get(index.value, member.metadata)
            raise RuntimeErrorLC(
                f"Invalid variable type {type(var)} for member expression",
                member.metadata,
            )
        if isinstance(member.object, MemberExpr):
            var = self._walk_reverse(member.object, env)
            if member.computed is True:
                index = self.evaluate(member.property, env)
            else:
                index = self._eval_member_property(member, env)
            if isinstance(var, NilValue):
                return var
            if isinstance(var, ArrayObject):
                return var.get(index.value, member.metadata)
            if isinstance(var, RecordObject):
                return var.get(index.value, member.metadata, NilValue())
            if isinstance(var, ObjectValue):
                return var.properties.get(index.value, NilValue())
            if isinstance(var, StringValue):
                return var.get(index.value, member.metadata)
            raise RuntimeErrorLC(
                f"Invalid variable type {type(var)} for member expression",
                member.metadata,
            )
        raise RuntimeErrorLC(
            f"Invalid member expression {member.object}", member.metadata
        )

    def _eval_member_property(self, member: MemberExpr, env: Env) -> IRuntimeValue:
        if member.computed is True:
            prop = self.evaluate(member.property, env)
        elif isinstance(member.property, Identifier):
            prop = StringValue(member.property.name, member.property.metadata, True)
        else:
            raise RuntimeErrorLC(
                f"Invalid object member property {member.property.kind.name}",
                member.metadata,
            )
        return prop

    def _member_property_is_new_element(self, member: MemberExpr) -> bool:
        if (
            member.property.kind == NodeKind.LIT_IDENT
            and isinstance(member.property, Identifier)
            and member.property.name == "[]"
        ):
            return True
        return False

    def _walk_member(self, member: MemberExpr, assign: bool, env: Env) -> IRuntimeValue:
        new_index = False
        if self._member_property_is_new_element(member) is True:
            new_index = True
            index = None
        else:
            index = self._eval_member_property(member, env)

        # sequence for assigning the member data
        if assign:
            if isinstance(member.object, Identifier):
                value = env.LookupVar(member.object.name, member.object.metadata)
            else:
                value = self._walk_reverse(member.object, env)
            if isinstance(value, ArrayObject):
                if new_index is True:
                    value.new_index = True
                    value.object_index = value.length
                    return value
                if index is None:
                    raise RuntimeErrorLC(
                        f"Invalid array element assignment, index is none",
                        member.metadata,
                    )
                value.object_index = int(index.value)
                return value
            if new_index is True:
                raise RuntimeErrorLC(
                    f"Invalid new array element assignment {value.type}",
                    member.metadata,
                )
            if (
                not isinstance(value, RecordObject)
                and not isinstance(value, ObjectValue)
                and not isinstance(value, StringValue)
            ):
                raise RuntimeErrorLC(
                    f"Invalid member assignment {value.type}", member.metadata
                )
            value.object_index = index.value  # type: ignore
            return value

        # sequence for reading the member data
        value = self._walk_reverse(member, env)
        if isinstance(value, ArrayObject):
            value.object_index = -1
            return value
        if isinstance(value, RecordObject) or isinstance(value, ObjectValue):
            value.object_index = ""
        return value

    def _eval_array_member_assign(
        self, lhs: ArrayObject, rhs: IRuntimeValue, op: str
    ) -> IRuntimeValue:
        if op == "=":
            lhs.set(lhs.object_index, rhs, lhs.metadata)  # type: ignore
        else:
            op = op[0]
            lhs.set(
                lhs.object_index,  # type: ignore
                self._eval_binary_expr(lhs.elements[lhs.object_index], rhs, op),  # type: ignore
                lhs.metadata,  # type: ignore
            )
        return rhs

    def _eval_record_member_assign(
        self, lhs: RecordObject, rhs: IRuntimeValue, op: str
    ) -> IRuntimeValue:
        if op == "=":
            lhs.fields[lhs.object_index] = rhs  # type: ignore
        else:
            op = op[0]
            lhs.fields[lhs.object_index] = self._eval_binary_expr(  # type: ignore
                lhs.fields[lhs.object_index], rhs, op  # type: ignore
            )
        return rhs

    def _eval_string_member_assign(
        self, lhs: StringValue, rhs: IRuntimeValue, op: str, metadata: NodeMetadata
    ) -> IRuntimeValue:
        if op != "=":
            raise RuntimeErrorLC(
                f"Arithmetic on a string? I don't think so! '{op}'",
                metadata,
            )
        if not isinstance(lhs.index, int):
            raise RuntimeErrorLC(f"Invalid string index type '{lhs.index}'", metadata)
        if lhs.index < 0 or lhs.index >= len(lhs.value):
            raise RuntimeErrorLC(f"String index out of bounds '{lhs.index}'", metadata)
        lhs.set(f"{lhs.value[:lhs.index]}{rhs.value}{lhs.value[lhs.index+1:]}")
        return rhs

    def _eval_record_member_new_element_assign(
        self, lhs: RecordObject, rhs: IRuntimeValue, op: str, metadata: NodeMetadata
    ) -> IRuntimeValue:
        if op == "=":
            lhs.fields[lhs.object_index] = rhs  # type: ignore
            return rhs
        raise RuntimeErrorLC(
            f"Invalid new record member assignment operator '{op}'",
            metadata,
        )

    def _eval_array_member_new_element_assign(
        self, lhs: ArrayObject, rhs: IRuntimeValue, op: str, metadata: NodeMetadata
    ) -> IRuntimeValue:
        if op == "=":
            lhs.append(rhs)
            return rhs
        raise RuntimeErrorLC(
            f"Invalid new array member assignment operator '{op}'", metadata
        )

    def _eval_member_assign(
        self, node: AssignmentExpr, member: MemberExpr, env: Env
    ) -> IRuntimeValue:

        lhs = self._walk_member(
            member=member,
            assign=True,
            env=env,
        )
        rhs = self.evaluate(node.value, env)
        op = node.operator

        if member.new_array_element is True:
            if isinstance(lhs, ArrayObject):
                return self._eval_array_member_new_element_assign(
                    lhs, rhs, op, node.metadata
                )
            if isinstance(lhs, RecordObject):
                return self._eval_record_member_new_element_assign(
                    lhs, rhs, op, node.metadata
                )

        if isinstance(lhs, ArrayObject):
            assign = self._eval_array_member_assign(lhs, rhs, op)
            return assign
        if isinstance(lhs, RecordObject):
            return self._eval_record_member_assign(lhs, rhs, op)
        if isinstance(lhs, StringValue):
            return self._eval_string_member_assign(lhs, rhs, op, node.metadata)
        raise RuntimeErrorLC(
            "Member assignment fell through the conditions", node.metadata
        )

    def _eval_assign(self, node: AssignmentExpr, env: Env) -> IRuntimeValue:
        if node.assignee.kind == NodeKind.LIT_IDENT and isinstance(
            node.assignee, Identifier
        ):
            return self._eval_var_assign(node, node.assignee, env)
        if node.assignee.kind == NodeKind.EXPR_MEMBER and isinstance(
            node.assignee, MemberExpr
        ):
            return self._eval_member_assign(node, node.assignee, env)
        raise RuntimeErrorLC(
            f"Invalid assignment target {node.assignee}", node.metadata
        )

    def _eval_array(self, node: ObjectLiteral, env: Env) -> IRuntimeValue:
        if not isinstance(node, ObjectLiteral) and node.okind != ObjectKind.ARRAY:
            raise RuntimeError(f"Invalid array literal {node}")
        if node.properties is None or len(node.properties) == 0:
            return ArrayObject(node.metadata)
        obj = ArrayObject(node.metadata)
        for prop in node.properties:
            obj.append(self.evaluate(prop, env))
        return obj

    def _eval_record(self, node: ObjectLiteral, env: Env) -> IRuntimeValue:
        if not isinstance(node, ObjectLiteral) and node.okind != ObjectKind.RECORD:
            raise RuntimeError(f"Invalid record literal {node}")
        if node.properties is None or len(node.properties) == 0:
            return RecordObject(node.metadata)
        obj = RecordObject(node.metadata)
        for prop in node.properties:
            if prop.key is None:
                raise RuntimeErrorLC(
                    f"Invalid record property {prop.key}", node.metadata
                )
            obj.properties[prop.key] = self.evaluate(prop, env)  #
        return obj

    def _eval_object(self, node: ObjectLiteral, env: Env) -> IRuntimeValue:
        if node.okind == ObjectKind.ARRAY:
            return self._eval_array(node, env)
        if node.okind == ObjectKind.RECORD:
            return self._eval_record(node, env)
        obj = ObjectValue({})
        for prop in node.properties:
            rv: IRuntimeValue
            if prop.value is None:
                rv = env.LookupVar(prop.key, prop.metadata)
            else:
                rv = self.evaluate(prop.value, env)
            obj.properties[prop.key] = rv
        return obj

    def __mconvert(self, value: IRuntimeValue) -> Any:
        """Converts a Macal value to a Python value."""
        if isinstance(value, list):
            return [self.__mconvert(val) for val in value]
        if isinstance(value, dict):
            return {key: self.__mconvert(val) for key, val in value.items()}
        if (
            value is None
            or value == "nil"
            or isinstance(value, str)
            or isinstance(value, dict)
            or isinstance(value, int)
            or isinstance(value, float)
            or isinstance(value, bool)
        ):
            return value
        if value.type in {
            ValueType.Integer,
            ValueType.Float,
            ValueType.Boolean,
            ValueType.String,
            ValueType.Nil,
        }:
            return value.value
        if isinstance(value, ArrayObject):
            return [self.__mconvert(val) for val in value.elements]
        if isinstance(value, RecordObject) or isinstance(value, ObjectValue):
            return {key: self.__mconvert(val) for key, val in value.properties.items()}

        if value.type == ValueType.NativeFunction and isinstance(
            value, NativeFunctionValue
        ):
            return value.callback
        raise RuntimeError(
            f"Invalid value type: {value.type.name} for conversion to Python."
        )

    def __pconvert(self, value: Any, env: Env) -> IRuntimeValue:
        """Converts a Python value to a Macal value."""
        if value is None or value == "nil":
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
                record.properties[key] = self.__pconvert(val, env)
            return record
        if isinstance(value, list):
            array = ArrayObject(NodeMetadata.new())
            for val in value:
                array.append(self.__pconvert(val, env))
            return array
        if isinstance(value, Coroutine):
            return NativeFunctionValue(value)  # type: ignore
        raise RuntimeError(f"Unknown Python value type: {type(value)}")

    def _eval_call(self, node: CallExpr, env: Env) -> IRuntimeValue:
        args: list[IRuntimeValue] = []
        func = self.evaluate(node.caller, env)
        for arg in node.args:
            args.append(self.evaluate(arg, env))
        if func.type == ValueType.NativeFunction:
            if not isinstance(func, NativeFunctionValue):
                raise RuntimeErrorLC(f"Can't call non-function value", node.metadata)
            native_args = [self.__mconvert(arg) for arg in args]
            return self.__pconvert(func.callback(*native_args), env)

        if func.type == ValueType.Function:
            if not isinstance(func, FunctionValue):
                raise RuntimeErrorLC("Can't call non-function value", node.metadata)
            scope: Env
            if func.env is None:
                scope = env.create_child_env(name=func.name)
                scope.is_in_function = True
            elif isinstance(func.env, Env):
                scope = func.env.create_child_env(name=func.name)
                if (
                    func.env.parent == None
                ):  # we are in global scope, we don't want to inherit from there.
                    scope.is_in_function = True
            if len(func.params) != len(args):
                raise RuntimeErrorLC(
                    f"Function {func.name} expects {len(func.params)} arguments, but got {len(args)}",
                    node.metadata,
                )
            for i in range(len(func.params)):
                scope.DeclareVar(func.params[i], args[i])
            result: IRuntimeValue = NilValue()
            for stmt in func.body:
                result = self.evaluate(stmt, scope)
                if result.type == ValueType.Return:
                    return result.value
                if result.type == ValueType.Halt:
                    return result
            return result
        raise RuntimeErrorLC("Can't call non-function value", node.metadata)

    def eval_program(self, program: ProgramNode, env: Env) -> IRuntimeValue:
        last_evaluated: IRuntimeValue = NilValue()
        for stmt in program.body:
            last_evaluated = self.evaluate(stmt, env)
            if isinstance(last_evaluated, IExpr):
                raise RuntimeErrorLC(
                    f"Runtime error: Last evaluated statement returned an expression instead of a runtime value! '{last_evaluated}'",
                    stmt.metadata,
                )

            if last_evaluated.type == ValueType.Halt:
                return last_evaluated
        return last_evaluated

    def _eval_var_decl(self, decl: VarDeclaration, env: Env) -> IRuntimeValue:
        value: IRuntimeValue
        if decl.value is not None:
            if decl.value.kind == NodeKind.LIT_NEW_ARRAY:
                value = ArrayObject(decl.value.metadata)
                return env.DeclareVar(decl.name, value, decl.metadata, decl.isconst)
            if decl.value.kind == NodeKind.LIT_NEW_RECORD:
                value = RecordObject(decl.value.metadata)
                return env.DeclareVar(decl.name, value, decl.metadata, decl.isconst)
            value = self.evaluate(decl.value, env)
        else:
            value = NilValue()
        return env.DeclareVar(decl.name, value, decl.metadata, decl.isconst)

    def _eval_func_decl(self, decl: FunctionDeclaration, env: Env) -> IRuntimeValue:
        if (
            decl.is_extern
            and decl.extern_module_name is not None
            and decl.extern_function_name is not None
        ):
            mod = env.LookupModule(decl.extern_module_name)
            if mod is None:
                if env.ImportModule(decl.extern_module_name, self.search_paths):
                    mod = env.LookupModule(decl.extern_module_name)
                if mod is None:
                    raise RuntimeErrorLC(
                        f"Module '{decl.extern_module_name}' not found, can't import function {decl.name}",
                        decl.metadata,
                    )
            function = mod.functions.get(decl.extern_function_name, None)
            if function is None:
                raise RuntimeErrorLC(
                    f"Function '{decl.extern_function_name}' not found in module '{decl.extern_module_name}'",
                    decl.metadata,
                )

            native_func = NativeFunctionValue(function)
            return env.DeclareVar(decl.name, native_func, decl.metadata, True)
        elif decl.is_extern:
            raise RuntimeErrorLC(
                f"Invalid extern function declaration {decl.name}", decl.metadata
            )
        func = FunctionValue(decl.name, decl.params, env, decl.body)
        return env.DeclareVar(decl.name, func, decl.metadata, True)

    def _eval_if(self, if_stmt: IfStatement, env: Env) -> IRuntimeValue:
        condition = self.evaluate(if_stmt.condition, env)
        if condition.type != ValueType.Boolean:
            raise RuntimeErrorLC(
                "Condition must be a boolean value.", if_stmt.condition.metadata
            )
        if condition.value is True:
            scope: Env = env.create_child_env()
            for stmt in if_stmt.body:
                result: IRuntimeValue = self.evaluate(stmt, scope)
                if (
                    result.type == ValueType.Halt
                    or result.type == ValueType.Return
                    or result.type == ValueType.Break
                    or result.type == ValueType.Continue
                ):
                    return result
            return NilValue()
        if len(if_stmt.elif_stmts) > 0:
            (ret, result) = self._eval_elif(if_stmt.elif_stmts, env)
            if ret is True:
                return result
        if if_stmt.else_stmt is not None:
            return self._eval_else(if_stmt.else_stmt, env)
        return NilValue()

    def _eval_elif(
        self, elif_stmts: list[ElifStatement], env: Env
    ) -> tuple[bool, IRuntimeValue]:
        for stmt in elif_stmts:
            condition = self.evaluate(stmt.condition, env)
            if condition.type != ValueType.Boolean:
                raise RuntimeErrorLC(
                    "Condition must be a boolean value.", stmt.metadata
                )
            if condition.value is True:
                scope: Env = env.create_child_env()
                for istmt in stmt.body:
                    result: IRuntimeValue = self.evaluate(istmt, scope)
                    if (
                        result.type == ValueType.Halt
                        or result.type == ValueType.Return
                        or result.type == ValueType.Break
                        or result.type == ValueType.Continue
                    ):
                        return (True, result)
                return (True, NilValue())
        return (False, NilValue())

    def _eval_else(self, else_stmt: ElseStatement, env: Env) -> IRuntimeValue:
        scope: Env = env.create_child_env()
        for stmt in else_stmt.body:
            result: IRuntimeValue = self.evaluate(stmt, scope)
            if (
                result.type == ValueType.Halt
                or result.type == ValueType.Return
                or result.type == ValueType.Break
                or result.type == ValueType.Continue
            ):
                return result
        return NilValue()

    def _eval_return(self, return_stmt: ReturnStatement, env: Env) -> IRuntimeValue:
        if return_stmt.value is not None:
            value = self.evaluate(return_stmt.value, env)
        else:
            value = NilValue()
        return ReturnValue(value)

    def _eval_halt(self, halt_stmt: HaltStatement, env: Env) -> IRuntimeValue:
        if halt_stmt.value is not None:
            value = self.evaluate(halt_stmt.value, env)
        else:
            value = NilValue()
        return HaltValue(value)

    def _eval_break(self, break_stmt: BreakStatement, env: Env) -> IRuntimeValue:
        return BreakValue()

    def _eval_continue(
        self, continue_stmt: ContinueStatement, env: Env
    ) -> IRuntimeValue:
        return ContinueValue()

    def _eval_while(self, while_stmt: WhileStatement, env: Env) -> IRuntimeValue:
        scope: Env = env.create_child_env()
        scope.is_in_loop = True
        while True:
            condition = self.evaluate(while_stmt.condition, env)
            if condition.type != ValueType.Boolean:
                raise RuntimeErrorLC(
                    "Condition must be a boolean value.", while_stmt.condition.metadata
                )
            if condition.value is False:
                break
            result: IRuntimeValue = NilValue()
            for stmt in while_stmt.body:
                result = self.evaluate(stmt, scope)
                if result.type == ValueType.Halt or result.type == ValueType.Return:
                    return result
                if result.type == ValueType.Break or result.type == ValueType.Continue:
                    break
            if result.type == ValueType.Break:
                break
        return NilValue()

    def _eval_foreach(self, foreach_stmt: ForEachStatement, env: Env) -> IRuntimeValue:
        scope: Env = env.create_child_env()
        scope.is_in_loop = True
        iterable = self.evaluate(foreach_stmt.iterable, env)
        if not iterable.iterable or not isinstance(iterable, IIterable):
            raise RuntimeErrorLC(
                "Value is not iterable.", foreach_stmt.iterable.metadata
            )
        scope.DeclareVar("it", NilValue(), NodeMetadata.new(), True)
        iterable.Reset()
        while True:
            it: IRuntimeValue = iterable.Next()
            if it is None or it.type == ValueType.Nil:
                break
            scope._set_const("it", it)
            for stmt in foreach_stmt.body:
                result = self.evaluate(stmt, scope)
                if result.type == ValueType.Halt or result.type == ValueType.Return:
                    return result
                if result.type == ValueType.Break or result.type == ValueType.Continue:
                    break
            if result.type == ValueType.Break:
                break
        return NilValue()

    def _run_matched_switch_case(
        self, case_stmt: CaseStatement, value: Any, env: Env
    ) -> Union[bool, IRuntimeValue]:
        scope: Env = env.create_child_env(f"{env.name}_switch_case_{value}")
        for stmt in case_stmt.body:
            result: IRuntimeValue = self.evaluate(stmt, scope)
            if result.type == ValueType.Halt or result.type == ValueType.Return:
                return result
            # with break we break out the switch statement case evaluations, otherwise we just continue with the next case
            if result.type == ValueType.Break:
                return True
        return False

    def _run_matched_default_case(
        self, default_stmt: DefaultCaseStatement, env: Env
    ) -> IRuntimeValue:
        scope: Env = env.create_child_env(f"{env.name}_switch_default")
        for stmt in default_stmt.body:
            result: IRuntimeValue = self.evaluate(stmt, scope)
            if result.type == ValueType.Halt or result.type == ValueType.Return:
                return result
        return NilValue()

    def _eval_switch(self, switch_stmt: SwitchStatement, env: Env) -> IRuntimeValue:
        switch_value = self.evaluate(switch_stmt.condition, env)
        did_not_break: bool = False
        for case_stmt in switch_stmt.cases:
            if case_stmt.kind == NodeKind.STMT_CASE and isinstance(
                case_stmt, CaseStatement
            ):
                case_value = self.evaluate(case_stmt.value, env)
                if case_value.value == switch_value.value or did_not_break:
                    result = self._run_matched_switch_case(
                        case_stmt, case_value.value, env
                    )
                    if result is True:
                        return NilValue()  # break out of the switch statement
                    if isinstance(result, IRuntimeValue) and (
                        result.type == ValueType.Halt or result.type == ValueType.Return
                    ):
                        return result  # halt happened, or we are returning from the function we are in.
                    did_not_break = True

        # When we get here we have to evaluate the default case if it exists
        if switch_stmt.default_case is not None and isinstance(
            switch_stmt.default_case, DefaultCaseStatement
        ):
            return self._run_matched_default_case(switch_stmt.default_case, env)
        return NilValue()

    def _eval_where_ex(self, where_expr: IExpr, source_data: ArrayObject, env: Env):
        scope = env.create_child_env(f"{env.name}_select_where")
        if isinstance(source_data.elements[0], RecordObject):
            sdr = source_data.elements[0]
            sdk = sdr.properties.keys()
        else:
            raise RuntimeErrorLC(
                f"Invalid source data for select statement, expected record, got {type(source_data.elements[0])}",
                where_expr.metadata,
            )
        for key in sdk:
            scope.DeclareVar(key, NilValue(), NodeMetadata.new(), True)
        where_filtered_data: ArrayObject = ArrayObject(where_expr.metadata)
        source_data.Reset()  # reset the iterator.
        while True:
            row = source_data.Next()
            if row is None or not isinstance(row, RecordObject):
                break
            for key, val in row.properties.items():
                scope._set_var(key, val)
            condition = self.evaluate(where_expr, scope)
            if condition.type != ValueType.Boolean:
                raise RuntimeErrorLC(
                    f"Where condition must be a boolean value {condition.type.name}",
                    where_expr.metadata,
                )
            if condition.value is True:
                where_filtered_data.append(row)
        return where_filtered_data

    def _filter_fields_ex(self, source: ArrayObject, fields: list[SelectField]):
        if len(fields) == 1 and fields[0].field == "*":
            return source
        source.Reset()  # reset the iterator.
        result: ArrayObject = ArrayObject(source.metadata)  # type: ignore
        while True:
            row = source.Next()
            if row is None or not isinstance(row, RecordObject):
                break
            new_row = RecordObject(row.metadata)  # type: ignore
            for field in fields:
                new_row.properties[field.alias] = row.properties.get(
                    field.field, NilValue()
                )
            result.append(new_row)
        return result

    def _merge_data_ex(
        self, origin_data: ArrayObject, from_data: ArrayObject
    ) -> ArrayObject:
        if not (
            isinstance(from_data, ArrayObject) and isinstance(origin_data, ArrayObject)
        ):
            raise RuntimeError(
                "MERGE: Type error, source and destination must be arrays."
            )
        if from_data.length >= 0 and origin_data.length == 0:
            return from_data  # .copy()
        if from_data.length == 0 and origin_data.length > 0:
            return origin_data  # .copy()
        elif (
            from_data.length == 1
            and origin_data.length == 1
            and set(from_data.elements[0].properties.keys()) != set(origin_data.elements[0].properties.keys())  # type: ignore
        ):
            keys = set().union(
                from_data.elements[0].columns, origin_data.elements[0].columns  # type: ignore
            )
            new_row: RecordObject = RecordObject(from_data.metadata)  # type: ignore
            nv = NilValue()
            for k in keys:
                new_row.properties[k] = from_data.elements[0].properties.get(k, nv)  # type: ignore
                v = origin_data.elements[0].properties.get(k, nv)  # type: ignore
                if v is not nv:
                    new_row.properties[k] = v
            final_data = ArrayObject(from_data.metadata)  # type: ignore
            final_data.append(new_row)
        # multiple records in each, with the same set of fields, then just append them both.
        elif set(from_data.elements[0].properties.keys()) == set(origin_data.elements[0].properties.keys()):  # type: ignore
            final_data = from_data.copy()
            for rec in origin_data.elements:  # type: ignore
                final_data.append(rec)
        # multiple records in each, but with different field sets, is an error.
        elif set(from_data.elements[0].properties.keys()) != set(origin_data.elements[0].properties.keys()):  # type: ignore
            return self._merge_data_unequal_fields_ex(from_data, origin_data)
        return final_data

    def _merge_data_unequal_fields(
        self, source: list[dict[str, Any]], destination: list[dict[str, Any]]
    ) -> list[dict[str, Any]]:
        source_fields = set(source[0].keys())
        destination_fields = set(destination[0].keys())
        merged_fields = source_fields.union(destination_fields)
        merged_data: list[dict[str, Any]] = []
        for row in destination:
            merged_item = {key: row.get(key, None) for key in merged_fields}
            merged_data.append(merged_item)
        for row in source:
            merged_item = {key: row.get(key, None) for key in merged_fields}
            merged_data.append(merged_item)
        return merged_data

    def _merge_data_unequal_fields_ex(
        self, source: ArrayObject, destination: ArrayObject
    ) -> ArrayObject:
        source_fields = set(source.elements[0].properties.keys())  # type: ignore
        destination_fields = set(destination.elements[0].properties.keys())  # type: ignore
        merged_fields = source_fields.union(destination_fields)
        merged_data: ArrayObject = ArrayObject(source.metadata)  # type: ignore
        nv = NilValue()
        for row in destination.elements:
            merged_item = RecordObject(row.metadata)  # type: ignore
            merged_item._properties = {
                key: row._properties.get(key, nv) for key in merged_fields  # type: ignore
            }
            merged_data.append(merged_item)
        for row in source.elements:
            merged_item = RecordObject(row.metadata)  # type: ignore
            merged_item._properties = {key: row._properties.get(key, nv) for key in merged_fields}  # type: ignore
            merged_data.append(merged_item)
        return merged_data

    def _python_type_to_macal_type(self, value: Any) -> str:
        if value is None:
            return "nil"
        if isinstance(value, bool):
            return "boolean"
        if isinstance(value, int):
            return "integer"
        if isinstance(value, float):
            return "float"
        if isinstance(value, str):
            return "string"
        if isinstance(value, list):
            return "array"
        if isinstance(value, dict):
            return "record"
        if isinstance(value, callable):  # type: ignore
            return "function"
        return "unknown"

    def _eval_select_ex(self, stmt: IStmt, env: Env) -> IRuntimeValue:
        if not isinstance(stmt, SelectStatement):
            raise RuntimeErrorLC("Invalid select statement", stmt.metadata)
        destination_data: Union[ArrayObject, RecordObject]
        merge = stmt.merge
        if merge is True:
            destination_data = self.evaluate(stmt.into_expr, env)  # type: ignore
            if destination_data is None:
                raise RuntimeErrorLC(
                    "Into variable not found for select statement",
                    stmt.into_expr.metadata,
                )
            if isinstance(destination_data, RecordObject):
                dd = ArrayObject(destination_data.metadata)  # type: ignore
                dd.append(destination_data)
                destination_data = dd
            elif not isinstance(destination_data, ArrayObject):
                raise RuntimeErrorLC(
                    f"Invalid destination data for select statement ({destination_data.type.name})",
                    stmt.into_expr.metadata,
                )
        else:
            destination_data = ArrayObject(stmt.into_expr.metadata)

        # at this point destination_data is an array.

        sd = self.evaluate(stmt.from_expr, env)
        source_data: ArrayObject
        if isinstance(sd, ArrayObject):
            source_data = sd
        elif isinstance(sd, RecordObject):
            source_data = ArrayObject(sd.metadata)  # type: ignore
            source_data.append(sd)
        else:
            source_data = ArrayObject(stmt.from_expr.metadata)  # type: ignore

        # at this point source_data is an array.

        if stmt.where_expr is not None and source_data.length > 0:
            source_data = self._eval_where_ex(stmt.where_expr, source_data, env)

        if source_data.length >= 1:
            source_data = self._filter_fields_ex(source_data, stmt.fields)

        if merge is True:
            destination_data = self._merge_data_ex(source_data, destination_data)  # type: ignore
            if destination_data.length == 1:
                destination_data = destination_data.elements[0]  # type: ignore
        else:
            destination_data = source_data

        if stmt.distinct is True:
            if (
                isinstance(destination_data, ArrayObject)
                and destination_data.length > 0
            ):
                destination_data = destination_data.elements[0]  # type: ignore
            if (
                isinstance(destination_data, RecordObject)
                and len(destination_data.columns) == 1
            ):
                destination_data = destination_data.properties[
                    destination_data.columns[0]
                ]  # type: ignore

        if isinstance(destination_data, ArrayObject) and (
            (stmt.distinct is True and destination_data.length > 0)
            # or (destination_data.length == 1)
        ):
            destination_data = destination_data.elements[0]  # type: ignore

        self._set_select_into(stmt.into_expr, destination_data, env)
        return NilValue()

    def _set_select_into(
        self, into: IExpr, rhs: IRuntimeValue, env: Env
    ) -> IRuntimeValue:

        if isinstance(into, Identifier):
            iev = env.Resolve(into.name)
            if iev is None:
                return env.DeclareVar(into.name, rhs, into.metadata)
            return env.AssignVar(into.name, rhs, into.metadata)
        if isinstance(into, MemberExpr):
            lhs = self._walk_member(
                member=into,
                assign=True,
                env=env,
            )
            op = "="
            if into.new_array_element is True:
                if isinstance(lhs, ArrayObject):
                    return self._eval_array_member_new_element_assign(
                        lhs, rhs, op, into.metadata
                    )
                if isinstance(lhs, RecordObject):
                    return self._eval_record_member_new_element_assign(
                        lhs, rhs, op, into.metadata
                    )

            if isinstance(lhs, ArrayObject):
                assign = self._eval_array_member_assign(lhs, rhs, op)
                return assign
            if isinstance(lhs, RecordObject):
                return self._eval_record_member_assign(lhs, rhs, op)
            if isinstance(lhs, StringValue):
                return self._eval_string_member_assign(lhs, rhs, op, into.metadata)

        raise RuntimeErrorLC(f"Invalid select into expression {into}", into.metadata)

    def _eval_include(self, stmt: IStmt, env: Env) -> IRuntimeValue:
        if stmt.kind == NodeKind.STMT_INCLUDE and isinstance(stmt, IncludeStatement):
            for liblit in stmt.value:
                lib = self.evaluate(liblit, env)
                if lib != NilValue():
                    env.DeclareVar(liblit.name, lib)
                else:
                    raise RuntimeErrorLC(
                        f"Runtime error: Library '{liblit.name}' not found.",
                        liblit.metadata,
                    )
            return NilValue()
        raise RuntimeErrorLC(
            f"Invalid include statement {stmt.kind.name}.", stmt.metadata
        )

    def _eval_library(self, stmt: LibraryLiteral, env: Env) -> IRuntimeValue:
        if stmt.kind == NodeKind.LIT_LIBRARY:
            if stmt.name is None:
                raise RuntimeErrorLC("Undefined library name.", stmt.metadata)
            the_lib = env.LookupVar(stmt.name, stmt.metadata, True)
            if the_lib.type != ValueType.Nil:
                return the_lib
            circular_reference: bool = False
            for path in self.search_paths:
                lib_path = os.path.join(path, stmt.name + DEFAULT_SOURCE_FILE_EXTENSION)
                if str(lib_path) == str(stmt.metadata.filename):
                    circular_reference = True
                    continue
                if os.path.exists(lib_path):
                    with open(lib_path, "r") as f:
                        source = f.read()
                    parser = Parser(lib_path)
                    program = parser.ProduceAST(source, False)
                    lib_env = env.get_global_env().create_child_env()
                    result = self.eval_program(program, lib_env)
                    if result.type == ValueType.Halt:
                        raise RuntimeErrorLC(
                            f"Library '{stmt.name}' import halted with exitcode {result.value}.",
                            stmt.metadata,
                        )
                    li = lib_env.LookupVar(f"{stmt.name}", stmt.metadata, True)
                    if li is not None and li.type != ValueType.Nil:
                        if isinstance(li, ObjectValue):
                            li.properties["path"] = StringValue(
                                lib_path, stmt.metadata, True
                            )
                            env.get_global_env().libraries[stmt.name] = lib_env
                            return li
                    nv = lib_env.DeclareVar(f"{stmt.name}", ObjectValue({}))
                    if isinstance(nv, ObjectValue):
                        nv.properties["name"] = StringValue(
                            stmt.name, stmt.metadata, True
                        )
                        nv.properties["version"] = StringValue("", stmt.metadata, True)
                        nv.properties["author"] = StringValue("", stmt.metadata, True)
                        nv.properties["email"] = StringValue("", stmt.metadata, True)
                        nv.properties["license"] = StringValue(
                            "MIT", stmt.metadata, True
                        )
                        nv.properties["description"] = StringValue(
                            "", stmt.metadata, True
                        )
                        nv.properties["external_module"] = StringValue(
                            "", stmt.metadata, True
                        )
                        nv.properties["path"] = StringValue(
                            lib_path, stmt.metadata, True
                        )
                        env.get_global_env().libraries[stmt.name] = lib_env
                        return nv
                    # This should now be unreachable.
                    raise RuntimeErrorLC(
                        f"Required Library Information Object not found for library {stmt.name}.",
                        stmt.metadata,
                    )
            if circular_reference is True:
                raise RuntimeErrorLC(
                    f"Library '{stmt.name}' cannot import itself.", stmt.metadata
                )
            raise RuntimeErrorLC(f"Library '{stmt.name}' not found.", stmt.metadata)
        raise RuntimeErrorLC("Invalid library literal.", stmt.metadata)

    def _eval_member(self, expr: MemberExpr, env: Env) -> IRuntimeValue:
        val = self._walk_member(member=expr, assign=False, env=env)
        return val

    def _eval_type(self, stmt: IStmt, env: Env) -> IRuntimeValue:
        if stmt.kind == NodeKind.STMT_TYPE:
            if isinstance(stmt, TypeStatement):
                xv = self.evaluate(stmt.expr, env)
                tn = str(xv.type.name).lower()
                if isinstance(xv, ArrayObject):
                    tn = "array"
                if isinstance(xv, RecordObject):
                    tn = "record"
                return StringValue(tn, stmt.metadata)
            raise RuntimeErrorLC(
                f"Invalid type statement ({type(stmt)})", stmt.metadata
            )
        raise RuntimeErrorLC(f"Invalid type statement ({stmt.kind})", stmt.metadata)

    def _eval_istype(self, stmt: IStmt, env: Env) -> IRuntimeValue:
        if stmt.kind == NodeKind.STMT_IS_TYPE:
            if isinstance(stmt, IsTypeStatement):
                xv = self.evaluate(stmt.expr, env)
                rv = BooleanValue(xv.type == stmt._type_to_check, stmt.metadata)
                if stmt._type_to_check == ValueType.Array:
                    rv = BooleanValue(isinstance(xv, ArrayObject), stmt.metadata)
                if stmt._type_to_check == ValueType.Record:
                    rv = BooleanValue(isinstance(xv, RecordObject), stmt.metadata)
                return rv
            raise RuntimeErrorLC(
                f"Invalid istype statement ({type(stmt)})", stmt.metadata
            )
        raise RuntimeErrorLC(f"Invalid istype statement ({stmt.kind})", stmt.metadata)

    def _eval_array_literal(self, stmt: IStmt, env: Env) -> IRuntimeValue:
        if stmt.kind == NodeKind.LIT_ARRAY:
            if isinstance(stmt, ArrayLiteral):
                arr = ArrayObject(stmt.metadata)
                for item in stmt.array:
                    arr.append(self.evaluate(item, env))
                return arr
            raise RuntimeErrorLC(f"Invalid array literal ({type(stmt)})", stmt.metadata)
        raise RuntimeErrorLC(f"Invalid array literal ({stmt.kind})", stmt.metadata)

    def _eval_record_literal(self, stmt: IStmt, env: Env) -> IRuntimeValue:
        if stmt.kind == NodeKind.LIT_RECORD:
            if isinstance(stmt, RecordLiteral):
                rec = RecordObject(stmt.metadata)
                for key, value in stmt.kvpairs:
                    k = self.evaluate(key, env)
                    if k.type != ValueType.String:
                        raise RuntimeErrorLC(
                            f"Invalid record key type ({k.type})", key.metadata
                        )
                    v = self.evaluate(value, env)
                    rec.properties[k.value] = v
                return rec
            raise RuntimeErrorLC(
                f"Invalid record literal ({type(stmt)})", stmt.metadata
            )
        raise RuntimeErrorLC(f"Invalid record literal ({stmt.kind})", stmt.metadata)

    def evaluate(self, stmt: IStmt, env: Env) -> IRuntimeValue:
        # Literals
        if stmt.kind == NodeKind.LIT_INT:
            if isinstance(stmt, IntLiteral):
                return IntegerValue(stmt.value)
            raise RuntimeErrorLC(
                f"Invalid integer literal ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.LIT_FLOAT:
            if isinstance(stmt, FloatLiteral):
                return FloatValue(stmt.value)
            raise RuntimeErrorLC(f"Invalid float literal ({type(stmt)})", stmt.metadata)
        if stmt.kind == NodeKind.LIT_STRING:
            if isinstance(stmt, StringLiteral):
                return StringValue(stmt.value, stmt.metadata, stmt.literal)
            raise RuntimeErrorLC(
                f"Invalid string literal  ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.LIT_IDENT:
            if isinstance(stmt, Identifier):
                return self._eval_identifier(stmt, env)
            raise RuntimeErrorLC(f"Invalid identifier ({type(stmt)})", stmt.metadata)
        if stmt.kind == NodeKind.LIT_OBJECT:
            if isinstance(stmt, ObjectLiteral):
                return self._eval_object(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid object literal ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.LIT_LIBRARY:
            if isinstance(stmt, LibraryLiteral):
                return self._eval_library(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid library literal ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.LIT_ARRAY:
            return self._eval_array_literal(stmt, env)
        if stmt.kind == NodeKind.LIT_RECORD:
            return self._eval_record_literal(stmt, env)
        if stmt.kind == NodeKind.LIT_NEW_ARRAY:
            return ArrayObject(stmt.metadata)
        if stmt.kind == NodeKind.LIT_NEW_RECORD:
            return RecordObject(stmt.metadata)

        # Expressions
        if stmt.kind == NodeKind.EXPR_ASSIGN:
            if isinstance(stmt, AssignmentExpr):
                return self._eval_assign(stmt, env)
            raise RuntimeErrorLC(
                "Invalid assignment expression  ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.EXPR_BINARY:
            if isinstance(stmt, BinaryExpr):
                return self._eval_binary(stmt, env)
            raise RuntimeErrorLC(
                "Invalid binary expression  ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.EXPR_UNARY:
            if isinstance(stmt, UnaryExpr):
                return self._eval_unary(stmt, env)
            raise RuntimeErrorLC(
                "Invalid unary expression  ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.EXPR_CALL:
            if isinstance(stmt, CallExpr):
                return self._eval_call(stmt, env)
            raise RuntimeErrorLC(
                "Invalid call expression  ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.EXPR_MEMBER:
            if isinstance(stmt, MemberExpr):
                return self._eval_member(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid member expression ({type(stmt)})", stmt.metadata
            )

        # Statements
        if stmt.kind == NodeKind.PROGRAM:
            if isinstance(stmt, ProgramNode):
                return self.eval_program(stmt, env)
            raise RuntimeErrorLC(f"Invalid program node ({type(stmt)})", stmt.metadata)
        if stmt.kind == NodeKind.VAR_DECL:
            if isinstance(stmt, VarDeclaration):
                return self._eval_var_decl(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid variable declaration ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.FUNC_DECL:
            if isinstance(stmt, FunctionDeclaration):
                return self._eval_func_decl(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid function declaration ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.STMT_IF:
            if isinstance(stmt, IfStatement):
                return self._eval_if(stmt, env)
            raise RuntimeErrorLC(f"Invalid if statement ({type(stmt)})", stmt.metadata)
        if stmt.kind == NodeKind.STMT_RETURN:
            if isinstance(stmt, ReturnStatement):
                return self._eval_return(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid return statement ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.STMT_HALT:
            if isinstance(stmt, HaltStatement):
                return self._eval_halt(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid halt statement ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.STMT_BREAK:
            if isinstance(stmt, BreakStatement):
                return self._eval_break(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid break statement ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.STMT_CONTINUE:
            if isinstance(stmt, ContinueStatement):
                return self._eval_continue(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid continue statement ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.STMT_WHILE:
            if isinstance(stmt, WhileStatement):
                return self._eval_while(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid while statement ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.STMT_FOREACH:
            if isinstance(stmt, ForEachStatement):
                return self._eval_foreach(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid foreach statement ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.STMT_SELECT:
            if isinstance(stmt, SelectStatement):
                return self._eval_select_ex(stmt, env)
            raise RuntimeErrorLC(
                f"Runtime error: Invalid select statement ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.STMT_SWITCH:
            if isinstance(stmt, SwitchStatement):
                return self._eval_switch(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid switch statement ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.STMT_INCLUDE:
            if isinstance(stmt, IncludeStatement):
                return self._eval_include(stmt, env)
            raise RuntimeErrorLC(
                f"Invalid include statement ({type(stmt)})", stmt.metadata
            )
        if stmt.kind == NodeKind.STMT_TYPE:
            return self._eval_type(stmt, env)
        if stmt.kind == NodeKind.STMT_IS_TYPE:
            return self._eval_istype(stmt, env)

        # Unknown statement kind
        raise RuntimeErrorLC(
            f"Unknown/unexpected statement: {stmt.kind.name} ({type(stmt)})",
            stmt.metadata,
        )

    def print(self, value: IRuntimeValue) -> None:
        print()
        print(f"Interpreter: Macal DSL Interpreter {__version__}")
        print()
        if value is not None:
            if value.type == ValueType.Nil:
                print("Command executed successfully")
            elif value.type == ValueType.Halt:
                if isinstance(value, HaltValue):
                    if value.exit_value is not None:
                        print(f"Program halted with exit value: {value.exit_value}")
                    else:
                        print("Program halted")
            else:
                print(value)
        else:
            print("No result")
