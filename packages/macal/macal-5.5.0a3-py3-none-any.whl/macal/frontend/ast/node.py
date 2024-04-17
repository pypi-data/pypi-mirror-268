# -*- coding: utf-8 -*-
#
# Product:   Macal
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

# AST nodes for the Macal language

from typing import Protocol, Optional, Any

from macal.frontend.ast.kind import NodeKind, ObjectKind
from macal.frontend.ast.metadata import NodeMetadata
from macal.runtime.value_type import ValueType


class IStmt(Protocol):
    """Interface for statement nodes in the AST."""

    @property
    def kind(self) -> NodeKind: ...
    @property
    def metadata(self) -> NodeMetadata: ...
    def json(self, nm: bool) -> dict: ...


# I hope this is the rigt way to avoid cyclic imports, otherwise i need valuetype to live in a separate module.


class IExpr(IStmt):
    """Interface for expression nodes in the AST."""


class Identifier(IExpr):
    """AST node representing an identifier."""

    def __init__(self, name: str, metadata: NodeMetadata) -> None:
        self._kind = NodeKind.LIT_IDENT
        self._name: str = name
        self._metadata = metadata

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def name(self) -> str:
        return self._name

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "name": self.name,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class ProgramNode(IStmt):
    """AST node representing the program."""

    def __init__(self) -> None:
        self._kind = NodeKind.PROGRAM
        self.body: list[IStmt] = []
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "body": [stmt.json(nm) for stmt in self.body],
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class VarDeclaration(IStmt):
    """AST node representing a variable declaration."""

    def __init__(
        self,
        name: Identifier,
        value: Optional[IExpr],
        isconst: bool,
        metadata: NodeMetadata,
    ) -> None:
        self._kind = NodeKind.VAR_DECL
        self._name: Identifier = name
        self.value: Optional[IExpr] = value
        self._isconst: bool = isconst
        self._metadata = metadata

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def name(self) -> str:
        return self._name.name

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    @property
    def isconst(self) -> bool:
        return self._isconst

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "name": self.name,
            "value": self.value.json(nm) if self.value else None,
            "isconst": self.isconst,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class FunctionDeclaration(IStmt):
    """AST node representing a function declaration."""

    def __init__(
        self,
        name: Identifier,
        params: list[str],
        body: list[IStmt],
        is_extern: bool = False,
        module_name: Optional[str] = None,
        function_name: Optional[str] = None,
    ) -> None:
        self._kind = NodeKind.FUNC_DECL
        self._name: Identifier = name
        self._params: list[str] = params
        self._body: list[IStmt] = body
        self._is_extern: bool = is_extern
        self._extern_module_name: Optional[str] = module_name
        self._extern_function_name: Optional[str] = function_name
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def name(self) -> str:
        return self._name.name

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    @property
    def params(self) -> list[str]:
        return self._params

    @property
    def body(self) -> list[IStmt]:
        return self._body

    @property
    def is_extern(self) -> bool:
        return self._is_extern

    @property
    def extern_module_name(self) -> Optional[str]:
        return self._extern_module_name

    @property
    def extern_function_name(self) -> Optional[str]:
        return self._extern_function_name

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "name": self.name,
            "params": self.params,
            "body": [stmt.json(nm) for stmt in self.body],
            "is_extern": self.is_extern,
            "extern_module_name": self.extern_module_name,
            "extern_function_name": self.extern_function_name,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class ReturnStatement(IStmt):
    """AST node representing a return statement."""

    def __init__(self, value: Optional[IExpr]) -> None:
        self._kind = NodeKind.STMT_RETURN
        self.value: Optional[IExpr] = value
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "value": self.value.json(nm) if self.value else None,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class ContinueStatement(IStmt):
    """AST node representing a continue statement."""

    def __init__(self) -> None:
        self._kind = NodeKind.STMT_CONTINUE
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class BreakStatement(IStmt):
    """AST node representing a break statement."""

    def __init__(self) -> None:
        self._kind = NodeKind.STMT_BREAK
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class HaltStatement(IStmt):
    """AST node representing a halt statement."""

    def __init__(self) -> None:
        self._kind = NodeKind.STMT_HALT
        self.value: Optional[IExpr] = None
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "value": self.value.json(nm) if self.value else None,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class ElifStatement(IStmt):
    """AST node representing an elif statement."""

    def __init__(
        self,
        condition: IExpr,
        body: list[IStmt],
    ) -> None:
        self._kind = NodeKind.STMT_ELIF
        self.condition: IExpr = condition
        self.body: list[IStmt] = body
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "condition": self.condition.json(nm),
            "body": [stmt.json(nm) for stmt in self.body],
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class ElseStatement(IStmt):
    """AST node representing an else statement."""

    def __init__(self, body: list[IStmt]) -> None:
        self._kind = NodeKind.STMT_ELSE
        self.body: list[IStmt] = body
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "body": [stmt.json(nm) for stmt in self.body],
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class IfStatement(IStmt):
    """AST node representing an if statement."""

    def __init__(
        self,
        condition: IExpr,
        body: list[IStmt],
        elifs: list[ElifStatement],
        elses: Optional[ElseStatement],
    ) -> None:
        self._kind = NodeKind.STMT_IF
        self.condition: IExpr = condition
        self.body: list[IStmt] = body
        self.elif_stmts: list[ElifStatement] = elifs
        self.else_stmt: Optional[ElseStatement] = elses
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "condition": self.condition.json(nm),
            "body": [stmt.json(nm) for stmt in self.body],
            "elifs": [stmt.json(nm) for stmt in self.elif_stmts],
            "else": self.else_stmt.json(nm) if self.else_stmt else None,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class WhileStatement(IStmt):
    """AST node representing a while statement."""

    def __init__(self, condition: IExpr, body: list[IStmt]) -> None:
        self._kind = NodeKind.STMT_WHILE
        self.condition: IExpr = condition
        self.body: list[IStmt] = body
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "condition": self.condition.json(nm),
            "body": [stmt.json(nm) for stmt in self.body],
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class ForEachStatement(IStmt):
    """AST node representing a foreach statement."""

    def __init__(self, iterable: IExpr, body: list[IStmt]) -> None:
        self._kind = NodeKind.STMT_FOREACH
        self.iterable: IExpr = iterable
        self.body: list[IStmt] = body
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "iterable": self.iterable.json(nm),
            "body": [stmt.json(nm) for stmt in self.body],
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class CaseStatement(IStmt):
    def __init__(self, value: IExpr, body: list[IStmt]) -> None:
        self._kind = NodeKind.STMT_CASE
        self.value: IExpr = value
        self.body: list[IStmt] = body
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "value": self.value.json(nm),
            "body": [stmt.json(nm) for stmt in self.body],
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class DefaultCaseStatement(IStmt):
    def __init__(self, body: list[IStmt]) -> None:
        self._kind = NodeKind.STMT_DEFAULT
        self.body: list[IStmt] = body
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "body": [stmt.json(nm) for stmt in self.body],
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class SwitchStatement(IStmt):
    """AST node representing a switch statement."""

    def __init__(
        self,
        condition: IExpr,
        cases: list[CaseStatement],
        default_case: Optional[DefaultCaseStatement],
    ) -> None:
        self._kind = NodeKind.STMT_SWITCH
        self.condition: IExpr = condition
        self.cases: list[CaseStatement] = cases
        self.default_case: Optional[DefaultCaseStatement] = default_case
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "condition": self.condition.json(nm),
            "cases": [stmt.json(nm) for stmt in self.cases],
            "default_case": self.default_case.json(nm) if self.default_case else None,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class SelectField:
    def __init__(self, field: str, alias: str, metadata: NodeMetadata) -> None:
        self.field: str = field
        self.alias: str = alias
        self._metadata = metadata


class SelectStatement(IStmt):
    def __init__(
        self,
        distinct: bool,
        fields: list[SelectField],
        from_expr: IExpr,
        where_expr: Optional[IExpr],
        merge: bool,
        into_expr: IExpr,
        into_var_name: str,
        metadata: NodeMetadata,
    ) -> None:
        self._kind = NodeKind.STMT_SELECT
        self.distinct: bool = distinct
        self.fields: list[SelectField] = fields
        self.from_expr: IExpr = from_expr
        self.where_expr: Optional[IExpr] = where_expr
        self.merge: bool = merge
        self.into_expr: IExpr = into_expr
        self.into_var_name: str = into_var_name
        self.orderby_expr: Optional[IExpr] = None  # for future expansion
        self._metadata = metadata

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "distinct": self.distinct,
            "fields": [
                {"field": field.field, "alias": field.alias} for field in self.fields
            ],
            "from_expr": self.from_expr.json(nm),
            "where_expr": self.where_expr.json(nm) if self.where_expr else "nil",
            "merge": self.merge,
            "into_expr": self.into_expr.json(nm),
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


# The linter is all kinds of weird about this one. It's complaining it not being defined if i put it at the end of the file.
class LibraryLiteral(IExpr):
    def __init__(self, name: str) -> None:
        self._kind = NodeKind.LIT_LIBRARY
        self._name: str = name
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    @property
    def name(self) -> str:
        return self._name

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "name": self.name,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class IncludeStatement(IStmt):
    """AST node representing an include statement."""

    def __init__(self, value: list[LibraryLiteral], metadata: NodeMetadata) -> None:
        self._kind = NodeKind.STMT_INCLUDE
        self._value: list[LibraryLiteral] = value
        self._metadata: NodeMetadata = metadata

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def value(self) -> list[LibraryLiteral]:
        return self._value

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "value": [stmt.json(nm) for stmt in self.value],
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class TypeStatement(IStmt):
    def __init__(self, expr: IExpr, metadata: NodeMetadata) -> None:
        self._kind = NodeKind.STMT_TYPE
        self._expr: IExpr = expr
        self._metadata = metadata

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def expr(self) -> IExpr:
        return self._expr

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[str, Any] = {
            "kind": self.kind.name,
            "expr": self.expr.json(nm),
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class IsTypeStatement(IStmt):
    def __init__(
        self, expr: IExpr, metadata: NodeMetadata, type_to_check: ValueType
    ) -> None:
        self._kind = NodeKind.STMT_IS_TYPE
        self._expr: IExpr = expr
        self._type_to_check: ValueType = type_to_check
        self._metadata = metadata

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def expr(self) -> IExpr:
        return self._expr

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[str, Any] = {
            "kind": self.kind.name,
            "expr": self.expr.json(nm),
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


# Expressions


class AssignmentExpr(IExpr):

    def __init__(
        self, assignee: IExpr, op: str, value: IExpr, metadata: NodeMetadata
    ) -> None:
        self._kind = NodeKind.EXPR_ASSIGN
        self.assignee: IExpr = assignee
        self.value: IExpr = value
        self.operator: str = op
        self._metadata = metadata

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "assignee": self.assignee.json(nm),
            "value": self.value.json(nm),
            "operator": self.operator,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class BinaryExpr(IExpr):
    def __init__(
        self, left: IExpr, right: IExpr, operator: str, metadata: NodeMetadata
    ) -> None:
        self._kind = NodeKind.EXPR_BINARY
        self.left: IExpr = left
        self.right: IExpr = right
        self.operator: str = operator
        self._metadata = metadata

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "left": self.left.json(nm),
            "right": self.right.json(nm),
            "operator": self.operator,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class UnaryExpr(IExpr):
    def __init__(self, right: IExpr, operator: str) -> None:
        self._kind = NodeKind.EXPR_UNARY
        self.right: IExpr = right
        self.operator: str = operator
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "right": self.right.json(nm),
            "operator": self.operator,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class MemberExpr(IExpr):
    def __init__(
        self, obj: IExpr, prop: IExpr, computed: bool, new_array_element: bool
    ) -> None:
        self._kind = NodeKind.EXPR_MEMBER
        self._object: IExpr = obj
        self.property: IExpr = prop
        self.computed: bool = computed
        self.new_array_element: bool = new_array_element
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def object(self) -> IExpr:
        return self._object

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "object": self.object.json(nm),
            "property": self.property.json(nm),
            "computed": self.computed,
            "new_array_element": self.new_array_element,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class CallExpr(IExpr):
    def __init__(self, caller: IExpr, args: list[IExpr]) -> None:
        self._kind = NodeKind.EXPR_CALL
        self.caller: IExpr = caller
        self.args: list[IExpr] = args
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "caller": self.caller.json(nm),
            "args": [arg.json(nm) for arg in self.args],
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


# Literals


class IntLiteral(IExpr):
    def __init__(self, value: int) -> None:
        self._kind = NodeKind.LIT_INT
        self.value: int = value
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "value": self.value,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class FloatLiteral(IExpr):
    def __init__(self, value: float) -> None:
        self._kind = NodeKind.LIT_FLOAT
        self.value: float = value
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "value": self.value,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class PropertyLiteral(IExpr):
    def __init__(self, key: str, value: Optional[IExpr]) -> None:
        self._kind = NodeKind.LIT_PROPERTY
        self.key: str = key
        self.value: Optional[IExpr] = value
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "key": self.key,
            "value": self.value.json(nm) if self.value else None,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class ObjectLiteral(IExpr):
    def __init__(self, properties: list[PropertyLiteral]) -> None:
        self._kind = NodeKind.LIT_OBJECT
        self._okind: ObjectKind = ObjectKind.OBJECT
        self.properties: list[PropertyLiteral] = properties
        self._metadata = NodeMetadata.new()

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def okind(self) -> ObjectKind:
        return self._okind

    @okind.setter
    def okind(self, kind: ObjectKind) -> None:
        self._okind = kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "okind": self.okind.name,
            "properties": [prop.json(nm) for prop in self.properties],
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class RecordLiteral(IExpr):
    def __init__(
        self, kvpairs: list[tuple[IExpr, IExpr]], metadata: NodeMetadata
    ) -> None:
        self._kind = NodeKind.LIT_RECORD
        self._okind: ObjectKind = ObjectKind.RECORD
        self._kvpairs: list[tuple[IExpr, IExpr]] = kvpairs
        self._metadata = metadata

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def okind(self) -> ObjectKind:
        return self._okind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    @property
    def kvpairs(self) -> list[tuple[IExpr, IExpr]]:
        return self._kvpairs

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "okind": self.okind.name,
            "kvpairs": [(k.json(nm), v.json(nm)) for k, v in self.kvpairs],  # type: ignore
        }
        if not nm and self.metadata:
            d["metadata"] = self._metadata.json()
        return d


class ArrayLiteral(IExpr):
    def __init__(self, array: list[IExpr], metadata: NodeMetadata) -> None:
        self._kind = NodeKind.LIT_ARRAY
        self._okind: ObjectKind = ObjectKind.RECORD
        self._array: list[IExpr] = array
        self._metadata = metadata

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def okind(self) -> ObjectKind:
        return self._okind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    @property
    def array(self) -> list[IExpr]:
        return self._array

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "okind": self.okind.name,
            "array": [el.json(nm) for el in self.array],
        }
        if not nm and self.metadata:
            d["metadata"] = self._metadata.json()
        return d


class StringLiteral(IExpr):
    def __init__(self, value: str, literal: bool = False) -> None:
        self._kind = NodeKind.LIT_STRING
        self.value: str = value
        self._metadata = NodeMetadata.new()
        self._literal: bool = literal

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    @property
    def literal(self) -> bool:
        return self._literal

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "value": self.value,
            "literal": self.literal,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class NewRecordLiteral(IExpr):
    def __init__(self, meta: NodeMetadata) -> None:
        self._kind = NodeKind.LIT_NEW_RECORD
        self._name = "new_record"
        self._metadata = meta

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def name(self) -> str:
        return self._name

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "name": self.name,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


class NewArrayLiteral(IExpr):
    def __init__(self, meta: NodeMetadata) -> None:
        self._kind = NodeKind.LIT_NEW_ARRAY
        self._name = "new_array"
        self._metadata = meta

    @property
    def kind(self) -> NodeKind:
        return self._kind

    @property
    def name(self) -> str:
        return self._name

    @property
    def metadata(self) -> NodeMetadata:
        return self._metadata

    def json(self, nm: bool) -> dict:
        d: dict[Any, Any] = {
            "kind": self.kind.name,
            "name": self.name,
        }
        if not nm and self.metadata:
            d["metadata"] = self.metadata.json()
        return d


# class StringInterpolationLiteral(IExpr):
#     def __init__(self, args: list[IExpr], metadata: NodeMetadata) -> None:
#         self._kind = NodeKind.LIT_STRING_INTERPOLATION
#         self.items: list[IExpr] = args
#         self._metadata = metadata
#
#     def json(self, nm: bool) -> dict:
#         d: dict[str, Any] = {
#             "kind": self.kind.name,
#             "items": [item.json(nm) for item in self.items],
#         }
#         if not nm and self.metadata:
#             d["metadata"] = self.metadata.json()
#         return d
#
#     @property
#     def kind(self) -> NodeKind:
#         return self._kind
#
#     @property
#     def metadata(self) -> NodeMetadata:
#         return self._metadata
