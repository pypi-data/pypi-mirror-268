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

# Parser for the Macal language

##############################################
#                                            #
#  TODO: Implement the SELECT statement      #
#  TODO: For the facilitating breaks in the  #
#        switch case bodies, implement a     #
#        flag to indicate that a break is    #
#        allowed in parsing statements.      #
#                                            #
##############################################

# Istmt
# IExpr
# Identifier
# ProgramNode
# VarDeclaration
# FunctionDeclaration
# ReturnStatement
# ContinueStatement
# BreakStatement
# HaltStatement
# IfStatement
# ElifStatement
# ElseStatement
# WhileStatement
# ForEachStatement
# SwitchStatement
# CaseStatement
# DefaultStatement
#
# AssignmentExpr
# BinaryExpr
# UnaryExpr
# MemberExpr
# CallExpr
#
# IntLiteral
# FloatLieteral
# PropertyLiteral
# ObjectLiteral
# StringLiteral

from typing import Optional, Tuple, Union
import sys
import json

# region AST imports

# region Statements import
from macal.frontend.ast.node import (
    ProgramNode,
    VarDeclaration,
    FunctionDeclaration,
    ReturnStatement,
    ContinueStatement,
    BreakStatement,
    HaltStatement,
    IfStatement,
    ElseStatement,
    ElifStatement,
    WhileStatement,
    ForEachStatement,
    SwitchStatement,
    CaseStatement,
    DefaultCaseStatement,
    IncludeStatement,
    TypeStatement,
    IsTypeStatement,
    SelectField,
    SelectStatement,
)

# endregion

# region Expressions import
from macal.frontend.ast.node import (
    AssignmentExpr,
    BinaryExpr,
    UnaryExpr,
    MemberExpr,
    CallExpr,
)

# endregion

# region Literals import
from macal.frontend.ast.node import (
    Identifier,
    IntLiteral,
    FloatLiteral,
    PropertyLiteral,
    ObjectLiteral,
    ArrayLiteral,
    RecordLiteral,
    StringLiteral,
    LibraryLiteral,
    NewArrayLiteral,
    NewRecordLiteral,
)

# endregion

from macal.frontend.ast.kind import ObjectKind, NodeKind
from macal.frontend.ast.node import IStmt, IExpr
from macal.frontend.ast.metadata import NodeMetadata

# endregion

from macal.frontend.mlexer import Token, Lexer, TokenKind
from macal.runtime.value_type import ValueType
from macal.mexceptions import SyntaxError
from macal.frontend.mparserstate import ParserState


class Parser:
    def __init__(self, filename: str) -> None:
        self._tokens: list[Token] = []
        self._current: int = 0
        self._length: int = 0
        self._filename: str = filename
        self._lexer_state: str = "none"
        self._parser_state: str = "initialized"
        self.program: Optional[ProgramNode] = None

    def _at(self, offset: int = 0) -> Token:
        if self._current + offset >= self._length:
            raise SyntaxError(
                "Unexpected end of file",
                NodeMetadata(-1, self._current + offset, self._filename),
            )
        return self._tokens[self._current + offset]

    def _eat(self) -> Token:
        self._current += 1
        return self._tokens[self._current - 1]

    def _not_eof(self) -> bool:
        return self._at().kind != TokenKind.EOF

    def _get_prev_meta(self) -> NodeMetadata:
        tok = self._at(-1)
        return NodeMetadata(tok.line, tok.column, self._filename)

    def _get_curr_meta(self) -> NodeMetadata:
        tok = self._at()
        return NodeMetadata(tok.line, tok.column, self._filename)

    def _get_meta(self, token: Token) -> NodeMetadata:
        return NodeMetadata(token.line, token.column, self._filename)

    def _expect(self, kind: TokenKind, message: str) -> Token:
        if self._at().kind != kind:
            raise SyntaxError(message, self._get_prev_meta())
        return self._eat()

    def _filter_tokens(self, tokens: list[Token]) -> list[Token]:
        return [
            token
            for token in tokens
            if token.kind not in [TokenKind.COMMENT, TokenKind.TYPE]
        ]

    def ProduceAST(
        self, source: str, debug: bool = False, state: Optional[ParserState] = None
    ) -> ProgramNode:
        lexer = Lexer()
        self._lexer_state = "initialized"
        self.tokens = lexer.lex(source, self._filename)
        self._lexer_state = "done"
        if debug:
            lexer.print()
        self._tokens = self._filter_tokens(self.tokens)
        self._length = len(self._tokens)
        self._current = 0
        self.program = ProgramNode()
        self._parser_state = "parsing"
        fn = self._filename
        if fn is None:
            fn = "unknown"
        global_state = state or ParserState(
            name="global", parent=None, filename=fn
        )  # global environment state.
        while self._not_eof():
            stmt: IStmt = self._parse_stmt(global_state)
            self.program.body.append(stmt)
        self._parser_state = "done"
        return self.program

    # ----------------------------------------- Statement Parsing -----------------------------------------

    def _set_stmt_metadata(self, node: IStmt, token: Token) -> None:
        node.metadata.line = token.line
        node.metadata.column = token.column
        node.metadata.filename = self._filename

    def _set_expr_metadata(self, node: IExpr, token: Token) -> None:
        node.metadata.line = token.line
        node.metadata.column = token.column
        node.metadata.filename = self._filename

    def _parse_stmt(self, state: ParserState) -> IStmt:
        if self._at().kind == TokenKind.CONST:
            return self._parse_var_declaration(is_const=True, state=state)
        if (
            self._at().kind == TokenKind.IDENTIFIER
            and self._at(1).kind != TokenKind.OPEN_PAREN
        ):
            return self._parse_assignment_statement(state)
        if self._at().kind == TokenKind.RETURN:
            if state.is_in_function is False and state.is_function_definition is False:
                raise SyntaxError("Unexpected 'return'.", self._get_curr_meta())
            return self._parse_return_statement(state)
        if self._at().kind == TokenKind.CONTINUE:
            if state.is_in_loop is False:
                raise SyntaxError(f"Unexpected 'continue'.", self._get_curr_meta())
            return self._parse_continue_statement(state)
        if self._at().kind == TokenKind.BREAK:
            if state.is_in_loop is False and state.is_in_switch is False:
                raise SyntaxError("Unexpected 'break'.", self._get_curr_meta())
            return self._parse_break_statement(state)
        if self._at().kind == TokenKind.HALT:
            return self._parse_halt_statement(state)
        if self._at().kind == TokenKind.IF:
            return self._parse_if_statement(state)
        if self._at().kind == TokenKind.ELSE:
            raise SyntaxError("Parser Error: Unexpected 'else'.", self._get_curr_meta())
        if self._at().kind == TokenKind.ELIF:
            raise SyntaxError(
                f"Parser Error: Unexpected 'elif'.", self._get_curr_meta()
            )
        if self._at().kind == TokenKind.WHILE:
            return self._parse_while_statement(state)
        if self._at().kind == TokenKind.FOREACH:
            return self._parse_for_each_statement(state)
        if self._at().kind == TokenKind.SWITCH:
            return self._parse_switch_statement(state)
        if self._at().kind == TokenKind.CASE:
            raise SyntaxError("Unexpected 'case'.", self._get_curr_meta())
        if self._at().kind == TokenKind.DEFAULT:
            raise SyntaxError("Unexpected 'default'.", self._get_curr_meta())
        if self._at().kind == TokenKind.INCLUDE:
            return self._parse_include_statement(state)
        if self._at().kind == TokenKind.TYPES:
            return self._parse_type_statement(state)
        if self._at().kind == TokenKind.ISTYPE:
            return self._parse_istype_statement(state)
        if self._at().kind == TokenKind.SELECT:
            return self._parse_select_statement(state)
        stmt: IStmt = self._parse_expr(state)
        self._expect(TokenKind.SEMICOLON, "Expected ';' after expression.")
        return stmt

    def _parse_function_declaration(self, state: ParserState) -> FunctionDeclaration:
        identifier: Identifier = self._parse_identifier(state)
        symbol = state.add_symbol(self._at(-1))
        decl_state = state.create_child(
            name=identifier.name, is_function_definition=True
        )
        self._expect(TokenKind.FN, "Function Declaration: Expected '=>' keyword.")
        args: list[IExpr] = self._parse_args(decl_state)
        params: list[str] = []
        for arg in args:
            if arg.kind != NodeKind.LIT_IDENT or not isinstance(arg, Identifier):
                raise SyntaxError(
                    "Function Declaration: Expected identifier in arguments.",
                    arg.metadata,
                )
            params.append(arg.name)
            token = Token()
            token.lexeme = arg.name
            token.column = arg.metadata.column
            token.line = arg.metadata.line
            token.kind = TokenKind.IDENTIFIER
            decl_state.add_symbol(token)
        body: list[IStmt] = []
        decl: FunctionDeclaration
        if self._at().kind == TokenKind.OPEN_BRACE:
            # standard function with a function body in Macal DSL
            self._expect(TokenKind.OPEN_BRACE, "Function Declaration: Expected '{'")

            while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
                stmt: IStmt = self._parse_stmt(decl_state)
                body.append(stmt)
            self._expect(TokenKind.CLOSE_BRACE, "Function Declaration: Expected '}'")
            decl = FunctionDeclaration(identifier, params, body)
        else:
            # external function declaration in Macal DSL
            ext = self._expect(
                TokenKind.EXTERNAL, "Function Declaration: Expected 'external'"
            )
            mod = self._expect(
                TokenKind.STRING,
                "External Function Declaration: Expected module identifier as string.",
            )
            self._expect(
                TokenKind.COMMA,
                "External Function Declaration: Expected ',' after module identifier.",
            )
            fun = self._expect(
                TokenKind.STRING,
                "External Function Declaration: Expected function identifier as string.",
            )
            self._expect(TokenKind.SEMICOLON, "Expected ';' after external function.")
            decl = FunctionDeclaration(
                identifier,
                params,
                body,
                is_extern=True,
                module_name=mod.lexeme,
                function_name=fun.lexeme,
            )
        decl.metadata.line = identifier.metadata.line
        decl.metadata.column = identifier.metadata.column
        decl.metadata.filename = self._filename
        return decl

    def _parse_identifier(self, state: ParserState) -> Identifier:
        token = self._expect(TokenKind.IDENTIFIER, "Expected identifier.")
        ident: Identifier = Identifier(token.lexeme, self._get_meta(token))
        return ident

    def _parse_return_statement(self, state: ParserState) -> ReturnStatement:
        ret = self._eat()
        if self._at().kind == TokenKind.SEMICOLON:
            stmt: ReturnStatement = ReturnStatement(None)
            self._set_stmt_metadata(stmt, ret)
            return stmt
        expr: IExpr = self._parse_expr(state)
        self._expect(TokenKind.SEMICOLON, "Expected ';' after return expression.")
        rstmt: ReturnStatement = ReturnStatement(expr)
        self._set_stmt_metadata(rstmt, ret)
        return rstmt

    def _parse_continue_statement(self, state: ParserState) -> ContinueStatement:
        cont = self._eat()
        self._expect(TokenKind.SEMICOLON, "Expected ';' after 'continue'.")
        stmt: ContinueStatement = ContinueStatement()
        self._set_stmt_metadata(stmt, cont)
        return stmt

    def _parse_break_statement(self, state: ParserState) -> BreakStatement:
        brk = self._eat()
        self._expect(TokenKind.SEMICOLON, "Expected ';' after 'break'.")
        stmt: BreakStatement = BreakStatement()
        self._set_stmt_metadata(stmt, brk)
        return stmt

    def _parse_halt_statement(self, state: ParserState) -> HaltStatement:
        halt = self._eat()
        if self._at().kind == TokenKind.SEMICOLON:
            stmt: HaltStatement = HaltStatement()
            self._set_stmt_metadata(stmt, halt)
            return stmt
        expr: IExpr = self._parse_expr(state)
        self._expect(TokenKind.SEMICOLON, "Expected ';' after 'halt'.")
        rstmt: HaltStatement = HaltStatement()
        rstmt.value = expr
        self._set_stmt_metadata(rstmt, halt)
        return rstmt

    def _parse_var_declaration(
        self, is_const: bool, state: ParserState
    ) -> VarDeclaration:
        if is_const:
            token = self._eat()  # eat 'const'
            meta = token
        else:
            meta = self._at()
        identifier: Identifier = self._parse_identifier(state)
        symbol_state = state.find_symbol(identifier.name)
        if symbol_state is not None:
            symbol = symbol_state.get_symbol(identifier.name)
            if is_const:
                if symbol is not None:
                    ameta = self._get_prev_meta()
                    if symbol.is_const:
                        raise SyntaxError(
                            f"Invalid const declaration at line {ameta.line} and column {ameta.column} in {ameta.filename}. Constant '{identifier.name}' already declared",
                            symbol.metadata,
                        )
                    else:
                        raise SyntaxError(
                            f"Invalid const declaration at line {ameta.line} and column {ameta.column} in {ameta.filename}, '{identifier.name}' is already declared as variable",
                            symbol.metadata,
                        )
                raise SyntaxError(
                    f"Constant '{identifier.name}' already declared",
                    self._get_prev_meta(),
                )
            raise SyntaxError(
                f"Variable/function '{identifier.name}' already declared",
                self._get_prev_meta(),
            )
        state.add_symbol(self._at(-1), is_const=is_const)
        if self._at().kind == TokenKind.SEMICOLON:
            self._eat()
            if is_const:
                raise SyntaxError(
                    "Must assign a value to a constant expression.",
                    self._get_prev_meta(),
                )
            # No value assigned to variable, it'll look weird but it's valid in Macal.
            decl: VarDeclaration = VarDeclaration(
                identifier, None, False, self._get_meta(meta)
            )
            return decl
        if self._at().kind != TokenKind.ASSIGN:
            raise SyntaxError(
                f"Variable '{identifier.name}' not found", self._get_prev_meta()
            )
        eq = self._eat()  # eat '='
        if eq.lexeme != "=":
            raise SyntaxError(
                f"Expected '=' after variable declaration, got '{eq.lexeme}'.",
                self._get_meta(eq),
            )
        value: IExpr = self._parse_expr(state)
        ch = self._at().lexeme
        if ch != ";":
            if value.kind == NodeKind.EXPR_BINARY:
                raise SyntaxError(
                    f"Expected ';' after variable declaration, got '{ch}'. \nPossible premature string termination",
                    self._get_curr_meta(),
                )
        self._expect(TokenKind.SEMICOLON, "Expected ';' after variable declaration.")
        rdecl: VarDeclaration = VarDeclaration(
            identifier, value, is_const, self._get_meta(meta)
        )
        return rdecl

    def _parse_if_statement(self, state: ParserState) -> IfStatement:
        if_token = self._eat()
        condition: IExpr = self._parse_expr(state)
        if condition.kind == NodeKind.EXPR_ASSIGN:
            raise SyntaxError(
                "Expected expression in if statement.", self._get_prev_meta()
            )
        self._expect(TokenKind.OPEN_BRACE, "Expected '{' after if condition.")
        body: list[IStmt] = []
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
            stmt: IStmt = self._parse_stmt(state)
            body.append(stmt)
        self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after if body.")
        elifs: list[ElifStatement] = []
        while self._not_eof() and self._at().kind == TokenKind.ELIF:
            elifs.append(self._parse_elif_statement(state))
        else_stmt: Optional[ElseStatement] = None
        if self._not_eof() and self._at().kind == TokenKind.ELSE:
            else_stmt = self._parse_else_statement(state)
        ifstmt: IfStatement = IfStatement(condition, body, elifs, else_stmt)
        self._set_stmt_metadata(ifstmt, if_token)
        return ifstmt

    def _parse_elif_statement(self, state: ParserState) -> ElifStatement:
        elif_token = self._eat()
        condition: IExpr = self._parse_expr(state)
        if condition.kind == NodeKind.EXPR_ASSIGN:
            raise SyntaxError(
                f"Expected expression in elif statement.", self._get_prev_meta()
            )
        self._expect(TokenKind.OPEN_BRACE, "Expected '{' after elif condition.")
        body: list[IStmt] = []
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
            stmt: IStmt = self._parse_stmt(state)
            body.append(stmt)
        self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after elif body.")
        elifstmt: ElifStatement = ElifStatement(condition, body)
        self._set_stmt_metadata(elifstmt, elif_token)
        return elifstmt

    def _parse_else_statement(self, state: ParserState) -> ElseStatement:
        else_token = self._eat()  # eat 'else'
        body: list[IStmt] = []
        if self._at().kind == TokenKind.OPEN_BRACE:
            self._eat()
            while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
                body.append(self._parse_stmt(state))
            self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after else body.")
            estmt = ElseStatement(body)
            self._set_stmt_metadata(estmt, else_token)
            return estmt
        body.append(self._parse_stmt(state))
        estmt = ElseStatement(body)
        self._set_stmt_metadata(estmt, else_token)
        return estmt

    def _parse_while_statement(self, state: ParserState) -> WhileStatement:
        while_token = self._eat()
        condition: IExpr = self._parse_expr(state)
        if condition.kind == NodeKind.EXPR_ASSIGN:
            raise SyntaxError(
                f"Expected expression in while statement", self._get_prev_meta()
            )
        self._expect(TokenKind.OPEN_BRACE, "Expected '{' after while condition.")
        body: list[IStmt] = []
        while_state = state.create_child(name=f"{state.name}_while", is_in_loop=True)
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
            body.append(self._parse_stmt(while_state))
        self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after while body.")
        wstmt: WhileStatement = WhileStatement(condition, body)
        self._set_stmt_metadata(wstmt, while_token)
        return wstmt

    def _parse_for_each_statement(self, state: ParserState) -> ForEachStatement:
        foreach_token = self._eat()
        iterable: IExpr = self._parse_expr(state)
        self._expect(TokenKind.OPEN_BRACE, "Expected '{' after foreach iterable.")
        body: list[IStmt] = []
        foreach_state = state.create_child(
            name=f"{state.name}_foreach", is_in_loop=True
        )
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
            body.append(self._parse_stmt(foreach_state))
        self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after foreach body.")
        fstmt: ForEachStatement = ForEachStatement(iterable, body)
        self._set_stmt_metadata(fstmt, foreach_token)
        return fstmt

    def _parse_switch_statement(self, state: ParserState) -> SwitchStatement:
        switch_token = self._eat()
        expr: IExpr = self._parse_expr(state)
        self._expect(TokenKind.OPEN_BRACE, "Expected '{' after switch expression.")
        cases: list[CaseStatement] = []
        default_case: Optional[DefaultCaseStatement] = None
        switch_state = state.create_child(
            name=f"{state.name}_switch", is_in_switch=True
        )
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
            if self._at().kind == TokenKind.CASE:
                cases.append(self._parse_case_statement(switch_state))
            elif self._at().kind == TokenKind.DEFAULT:
                if default_case is not None:
                    raise SyntaxError("Unexpected 'default'.", self._get_curr_meta())
                default_case = self._parse_default_case_statement(switch_state)
            else:
                raise SyntaxError(
                    f"Unexpected token ({self._at().kind.name}) in switch statement.",
                    self._get_curr_meta(),
                )
        self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after switch body.")
        sstmt: SwitchStatement = SwitchStatement(expr, cases, default_case)
        self._set_stmt_metadata(sstmt, switch_token)
        return sstmt

    def _parse_case_statement(self, state: ParserState) -> CaseStatement:
        case_token = self._eat()
        expr: IExpr = self._parse_expr(state)
        self._expect(TokenKind.COLON, "Expected ':' after case expression.")
        self._expect(TokenKind.OPEN_BRACE, "Expected '{' after case expression.")
        body: list[IStmt] = []
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
            body.append(self._parse_stmt(state))
        self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after case body.")
        cstmt: CaseStatement = CaseStatement(expr, body)
        self._set_stmt_metadata(cstmt, case_token)
        return cstmt

    def _parse_default_case_statement(self, state: ParserState) -> DefaultCaseStatement:
        default_token = self._eat()
        self._expect(TokenKind.COLON, "Expected ':' after default.")
        self._expect(TokenKind.OPEN_BRACE, "Expected '{' after default.")
        body: list[IStmt] = []
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
            body.append(self._parse_stmt(state))
        self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after default body.")
        dstmt: DefaultCaseStatement = DefaultCaseStatement(body)
        self._set_stmt_metadata(dstmt, default_token)
        return dstmt

    def _parse_include_statement(self, state: ParserState) -> IncludeStatement:
        tok = self._eat()  # eat 'include'
        if self._at().kind != TokenKind.IDENTIFIER:
            raise SyntaxError(
                "Expected library identifier after include.", self._get_prev_meta()
            )
        libs: list[LibraryLiteral] = []
        while self._not_eof() and self._at().kind != TokenKind.SEMICOLON:
            ltok = self._expect(TokenKind.IDENTIFIER, "Expected library identifier.")
            lib = LibraryLiteral(ltok.lexeme)
            glob_state = state.get_global()
            if not glob_state.find_symbol(ltok.lexeme):
                glob_state.add_symbol(ltok, is_const=True)
            self._set_expr_metadata(lib, ltok)
            libs.append(lib)
            state.add_symbol(ltok)
            if self._at().kind != TokenKind.SEMICOLON:
                self._expect(TokenKind.COMMA, "Expected ',' after library identifier.")
        self._expect(TokenKind.SEMICOLON, "Expected ';' after include statement.")
        stmt = IncludeStatement(libs, self._get_meta(tok))
        return stmt

    def _parse_type_statement(
        self,
        state: ParserState,
        as_expr: bool = False,
    ) -> TypeStatement:
        tok = self._eat()
        self._expect(TokenKind.OPEN_PAREN, "Expected '(' after 'Type'.")
        expr = self._parse_expr(state)
        self._expect(TokenKind.CLOSE_PAREN, "Expected ')' after 'Type'.")
        if not as_expr:
            self._expect(TokenKind.SEMICOLON, "Expected ';' after type statement.")
        stmt = TypeStatement(expr, self._get_meta(tok))
        return stmt

    def _parse_istype_statement(
        self, state: ParserState, as_expr=True
    ) -> IsTypeStatement:
        tok = self._eat()
        ttc: ValueType = ValueType.Nil
        if tok.lexeme == "IsRecord" or tok.lexeme == "isRecord":
            ttc = ValueType.Record
        elif tok.lexeme == "IsArray" or tok.lexeme == "isArray":
            ttc = ValueType.Array
        elif tok.lexeme == "IsString" or tok.lexeme == "isString":
            ttc = ValueType.String
        elif tok.lexeme == "IsInt" or tok.lexeme == "isInt":
            ttc = ValueType.Integer
        elif tok.lexeme == "IsInteger" or tok.lexeme == "isInteger":
            ttc = ValueType.Integer
        elif tok.lexeme == "IsFloat" or tok.lexeme == "isFloat":
            ttc = ValueType.Float
        elif tok.lexeme == "IsBool" or tok.lexeme == "isBool":
            ttc = ValueType.Boolean
        elif tok.lexeme == "IsNil" or tok.lexeme == "isNil":
            ttc = ValueType.Nil
        elif tok.lexeme == "IsFunction" or tok.lexeme == "isFunction":
            ttc = ValueType.Function
        elif tok.lexeme == "IsObject" or tok.lexeme == "isObject":
            ttc = ValueType.Object
        else:
            raise SyntaxError(
                f"Invalid 'Is<Type>' keyword ({tok.lexeme})", self._get_prev_meta()
            )
        self._expect(TokenKind.OPEN_PAREN, "Expected '(' after 'Type'.")
        expr = self._parse_expr(state)
        self._expect(TokenKind.CLOSE_PAREN, "Expected '(' after 'Type'.")
        if not as_expr:
            self._expect(TokenKind.SEMICOLON, "Expected ';' after type statement.")
        stmt = IsTypeStatement(expr, self._get_meta(tok), ttc)
        return stmt

    def _parse_assignment_statement(self, state: ParserState) -> IStmt:
        if self._at(1).kind == TokenKind.FN:
            return self._parse_function_declaration(state)
        varname = self._at().lexeme
        if (
            state.find_symbol(varname) is not None or varname == "it"
        ):  # 'it' is a reserved keyword in Macal, it's used in the foreach statement.
            expr = self._parse_assignment_expr(state)
            self._expect(TokenKind.SEMICOLON, "Expected ';' after assignment.")
            return expr
        vardecl = self._parse_var_declaration(is_const=False, state=state)
        return vardecl

    def _parse_select_statement(self, state: ParserState) -> IStmt:
        token = self._expect(TokenKind.SELECT, "Expected 'select' keyword.")
        distinct = self._at().lexeme == "distinct"
        if distinct is True:
            self._eat()
        fields: list[SelectField] = []
        while self._at().kind == TokenKind.IDENTIFIER:
            field = self._eat()
            alias = field
            if self._at().kind == TokenKind.AS:
                self._eat()
                alias = self._eat()
            fields.append(
                SelectField(field.lexeme, alias.lexeme, self._get_meta(field))
            )
            if self._at().kind == TokenKind.COMMA:
                self._eat()
        if (
            len(fields) == 0
            and self._at().kind == TokenKind.BINARYOPERATOR
            and self._at().lexeme == "*"
        ):
            fields.append(SelectField("*", "*", self._get_meta(self._eat())))
        self._expect(TokenKind.FROM, "Expected 'from' keyword.")
        from_expr = self._parse_expr(state)
        where_expr: Optional[IExpr] = None
        if self._at().kind == TokenKind.WHERE:
            self._eat()
            where_expr = self._parse_expr(state)
        merge = self._at().kind == TokenKind.MERGE
        if merge:
            self._eat()
        self._expect(TokenKind.INTO, "Expected 'into' keyword.")
        into_var_name = self._at()
        into_expr = self._parse_expr(state)
        into_name = into_var_name.lexeme
        if (
            into_expr.kind != NodeKind.LIT_IDENT
            and into_expr.kind != NodeKind.EXPR_MEMBER
        ):
            raise SyntaxError(
                f"Invalid into expression kind ({into_expr.kind.name})",
                self._get_prev_meta(),
            )
        self._expect(TokenKind.SEMICOLON, "Expected ';' after select statement.")
        return SelectStatement(
            distinct,
            fields,
            from_expr,
            where_expr,
            merge,
            into_expr,
            into_var_name.lexeme,
            self._get_meta(token),
        )

    # ----------------------------------------- Expression Parsing -----------------------------------------

    def _parse_expr(self, state: ParserState) -> IExpr:
        return self._parse_assignment_expr(state)

    def _parse_assignment_expr(self, state: ParserState) -> IExpr:
        token = self._at()
        left: IExpr = self._parse_string_concatenation(state)
        if isinstance(left, Identifier):
            if state.find_symbol(left.name) is None:
                state.add_symbol(token)
        if self._at().lexeme in {"=", "+=", "-=", "*=", "/=", "%=", "^=", ".="}:
            op_token = self._eat()
            if left.kind != NodeKind.LIT_IDENT and left.kind != NodeKind.EXPR_MEMBER:
                raise SyntaxError(
                    "Invalid assignment target (left)",
                    NodeMetadata(token.line, token.column, self._filename),
                )
            right: IExpr = self._parse_assignment_expr(state)
            expr: AssignmentExpr = AssignmentExpr(
                left, op_token.lexeme, right, self._get_meta(token)
            )
            return expr
        return left

    def _parse_string_concatenation(self, state: ParserState) -> IExpr:
        left: IExpr = self._parse_object_expr(state)
        while (
            self._not_eof()
            and self._at().kind == TokenKind.BINARYOPERATOR
            and self._at().lexeme in {"+."}
        ):
            op_token = self._eat()  # eat '+' or '-' token
            right: IExpr = self._parse_object_expr(state)
            left = BinaryExpr(
                left=left,
                operator=op_token.lexeme,
                right=right,
                metadata=right.metadata,
            )
            self._set_expr_metadata(left, op_token)
        return left

    def _parse_object_expr(self, state: ParserState) -> IExpr:
        if self._at().kind != TokenKind.OBJECT:
            return self._parse_array_expr(state)
        obj = self._eat()  # eat 'object'
        self._expect(TokenKind.OPEN_BRACE, "Expected '{' after 'object'.")
        properties: list[PropertyLiteral] = []
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
            # { key: value, key: value, ... }
            key = self._expect(
                TokenKind.IDENTIFIER, "Expected identifier for object property key."
            )
            # this allows for shorhand key, key -> { key, key, ... }
            if self._at().kind == TokenKind.COMMA:
                self._eat()  # eat ','
                prop = PropertyLiteral(key.lexeme, None)
                self._set_expr_metadata(prop, key)
                properties.append(prop)
                continue
            # this allows for shorthand key -> { key }
            if self._at().kind == TokenKind.CLOSE_BRACE:
                prop = PropertyLiteral(key.lexeme, None)
                self._set_expr_metadata(prop, key)
                properties.append(prop)
                break
            # { key: value }
            self._expect(TokenKind.COLON, "Expected ':' after object property key.")
            value = self._parse_expr(state)
            prop = PropertyLiteral(key.lexeme, value)
            self._set_expr_metadata(prop, key)
            properties.append(prop)
            if self._at().kind != TokenKind.CLOSE_BRACE:
                self._expect(TokenKind.COMMA, "Expected ',' after object property.")
        self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after object properties.")
        objexpr = ObjectLiteral(properties)
        self._set_expr_metadata(objexpr, obj)
        return objexpr

    def _parse_array_expr(self, state: ParserState) -> IExpr:
        if self._at().kind != TokenKind.OPEN_BRACKET:
            return self._parse_record_expr(state)
        arr = self._eat()  # eat '['
        elements: list[IExpr] = []
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACKET:
            elements.append(self._parse_expr(state))
            if self._at().kind != TokenKind.CLOSE_BRACKET:
                self._expect(TokenKind.COMMA, "Expected ',' after array element.")
        self._expect(TokenKind.CLOSE_BRACKET, "Expected ']' after array elements.")
        arrlit = ArrayLiteral(elements, self._get_meta(arr))
        return arrlit

    def _parse_record_expr(self, state: ParserState) -> IExpr:
        if self._at().kind != TokenKind.OPEN_BRACE:
            return self._parse_logical_expr(state)
        rec = self._eat()  # eat '{'
        kvpairs: list[tuple[IExpr, IExpr]] = []
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
            key = self._parse_expr(state)
            self._expect(TokenKind.COLON, "Expected ':' after record key.")
            value = self._parse_expr(state)
            kvpairs.append((key, value))
            if self._at().kind != TokenKind.CLOSE_BRACE:
                self._expect(TokenKind.COMMA, "Expected ',' after record value.")
        self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after record values.")
        reclit = RecordLiteral(kvpairs, self._get_meta(rec))
        return reclit

    def _parse_logical_expr(self, state: ParserState) -> IExpr:
        left: IExpr = self._parse_comparison_expr(state)
        while self._not_eof() and self._at().kind in {
            TokenKind.AND,
            TokenKind.OR,
            TokenKind.XOR,
        }:  # 'and', 'or', 'xor' , '&&', '||', '^^'
            op_token = self._eat()
            right: IExpr = self._parse_comparison_expr(state)
            left = BinaryExpr(
                left=left,
                operator=op_token.lexeme,
                right=right,
                metadata=right.metadata,
            )
            self._set_expr_metadata(left, op_token)
        return left

    def _parse_comparison_expr(self, state: ParserState) -> IExpr:
        left: IExpr = self._parse_addition_expr(state)
        while self._not_eof() and (
            self._at().kind == TokenKind.BINARYOPERATOR
            and self._at().lexeme in {"<", "<=", ">", ">=", "==", "!="}
        ):
            op_token = self._eat()
            right: IExpr = self._parse_addition_expr(state)
            left = BinaryExpr(
                left=left,
                operator=op_token.lexeme,
                right=right,
                metadata=right.metadata,
            )
            self._set_expr_metadata(left, op_token)
        return left

    def _parse_addition_expr(self, state: ParserState) -> IExpr:
        left: IExpr = self._parse_multiplication_expr(state)
        while (
            self._not_eof()
            and self._at().kind == TokenKind.BINARYOPERATOR
            and self._at().lexeme in {"+", "-"}
        ):
            op_token = self._eat()  # eat '+' or '-' token
            right: IExpr = self._parse_multiplication_expr(state)
            left = BinaryExpr(
                left=left,
                operator=op_token.lexeme,
                right=right,
                metadata=right.metadata,
            )
            self._set_expr_metadata(left, op_token)
        return left

    def _parse_multiplication_expr(self, state: ParserState) -> IExpr:
        left: IExpr = self._parse_power_expr(state)

        while (
            self._not_eof()
            and self._at().kind == TokenKind.BINARYOPERATOR
            and self._at().lexeme in {"*", "/", "%"}
        ):
            op_token = self._eat()  # eat '*', '/', or '%' token
            right: IExpr = self._parse_power_expr(state)
            left = BinaryExpr(
                left=left,
                operator=op_token.lexeme,
                right=right,
                metadata=right.metadata,
            )
            self._set_expr_metadata(left, op_token)
        return left

    def _parse_power_expr(self, state: ParserState) -> IExpr:
        left: IExpr = self._parse_unary_expr(state)
        while (
            self._not_eof()
            and self._at().kind == TokenKind.BINARYOPERATOR
            and self._at().lexeme == "^"
        ):
            op_token = self._eat()
            right: IExpr = self._parse_unary_expr(state)
            left = BinaryExpr(
                left=left,
                operator=op_token.lexeme,
                right=right,
                metadata=right.metadata,
            )
            self._set_expr_metadata(left, op_token)
        return left

    def _parse_unary_expr(self, state: ParserState) -> IExpr:
        op_token = self._at()
        if (
            op_token.kind == TokenKind.NOT
            or op_token.kind == TokenKind.BINARYOPERATOR
            and op_token.lexeme
            in {
                "-",
                "++",
                "--",
            }
        ):
            self._eat()
            right: IExpr = self._parse_unary_expr(state)
            expr: UnaryExpr = UnaryExpr(operator=op_token.lexeme, right=right)
            self._set_expr_metadata(expr, op_token)
            return expr
        return self._parse_call_member_expr(state)

    def _parse_call_member_expr(self, state: ParserState) -> IExpr:
        member: IExpr = self._parse_member_expr(state)
        if self._at().kind == TokenKind.OPEN_PAREN:
            return self._parse_call_expr(member, state)
        return member

    def _parse_call_expr(self, callee: IExpr, state: ParserState) -> CallExpr:
        tok = self._at(-1)
        cexpr: CallExpr = CallExpr(caller=callee, args=self._parse_args(state))
        self._set_expr_metadata(cexpr, tok)
        if self._at().kind == TokenKind.OPEN_PAREN:
            cexpr = self._parse_call_expr(cexpr, state)
        return cexpr

    def _parse_args(self, state: ParserState) -> list[IExpr]:
        self._expect(TokenKind.OPEN_PAREN, "Expected '(' after function identifier.")
        args: list[IExpr] = []
        if self._at().kind != TokenKind.CLOSE_PAREN:
            args = self._parse_args_list(state)
        self._expect(TokenKind.CLOSE_PAREN, "Expected ')' after function arguments.")
        return args

    def _parse_args_list(self, state: ParserState) -> list[IExpr]:
        args: list[IExpr] = [self._parse_expr(state)]
        while self._not_eof() and self._at().kind == TokenKind.COMMA:
            self._eat()  # eat ',' after argument
            if state.is_function_definition:
                # add function argument to symbol table, making the assumption it's a valid identifier.
                state.add_symbol(self._at())
            args.append(self._parse_expr(state))
        return args

    def _parse_member_expr(self, state: ParserState) -> IExpr:
        obj: IExpr = self._parse_primary_expr(state)
        while self._at().kind in {TokenKind.DOT, TokenKind.OPEN_BRACKET}:
            op = self._eat()
            prop: IExpr
            computed: bool = False
            # non-computed values aka obj.expr
            if op.kind == TokenKind.DOT:
                computed = False
                prop = self._parse_primary_expr(state)
                if prop.kind != NodeKind.LIT_IDENT:
                    raise SyntaxError(
                        f"Can not use '.' operator with non-identifier value ({prop})",
                        self._get_prev_meta(),
                    )
            else:  # this allows obj[computedValue]
                computed = True
                if self._at().kind == TokenKind.CLOSE_BRACKET:
                    return self._parse_new_array_element(obj, state)
                prop = self._parse_expr(state)
                self._expect(
                    TokenKind.CLOSE_BRACKET,
                    "Expected ']' after computed property.",
                )

            obj = MemberExpr(
                obj=obj, prop=prop, computed=computed, new_array_element=False
            )
            self._set_expr_metadata(obj, op)
        return obj

    def _parse_new_array_element(
        self, obj: IExpr, state: ParserState
    ) -> AssignmentExpr:
        tobj = self._expect(
            TokenKind.CLOSE_BRACKET, "Expected ']' after computed property."
        )
        op = self._expect(TokenKind.ASSIGN, "Expected '=' after computed property.")
        if op.lexeme != "=":
            raise SyntaxError(
                "Expected '=' after computed property.", self._get_prev_meta()
            )
        value: IExpr = self._parse_expr(state)
        member = MemberExpr(
            obj=obj,
            prop=Identifier("[]", self._get_meta(op)),
            computed=True,
            new_array_element=True,
        )
        self._set_expr_metadata(member, tobj)
        asgn = AssignmentExpr(
            assignee=member, op="=", value=value, metadata=self._get_meta(tobj)
        )
        return asgn

    def _parse_primary_expr(self, state: ParserState) -> IExpr:
        token = self._at()
        if token.kind == TokenKind.IDENTIFIER:
            return self._parse_identifier(state)
        if token.kind == TokenKind.INTEGER:
            return self._parse_int_literal(state)
        if token.kind == TokenKind.FLOAT:
            return self._parse_float_literal(state)
        if token.kind == TokenKind.STRING:
            return self._parse_string_literal(state)
        if token.kind == TokenKind.OPEN_PAREN:  # (expr)
            self._eat()
            expr: IExpr = self._parse_expr(state)
            self._expect(TokenKind.CLOSE_PAREN, "Expected ')' after expression.")
            return expr
        if token.kind == TokenKind.ARRAY:
            if self._at(1).kind == TokenKind.IDENTIFIER:
                self._eat()  # eat 'array' because it is used as a type and we don't handle that yet.
                return self._parse_identifier(state)
            return self._parse_array_literal(state)
        if token.kind == TokenKind.RECORD:
            if self._at(1).kind == TokenKind.IDENTIFIER:
                self._eat()  # eat 'record' because it is used as a type and we don't handle that yet.
                return self._parse_identifier(state)
            return self._parse_record_literal(state)
        if token.kind == TokenKind.TYPES:
            return self._parse_type_statement(state, as_expr=True)  # type: ignore
        if token.kind == TokenKind.ISTYPE:
            return self._parse_istype_statement(state, as_expr=True)  # type: ignore
        raise SyntaxError(
            f"Unexpected token ({token.lexeme}) in expression.",
            NodeMetadata(token.line, token.column, self._filename),
        )

    def _parse_int_literal(self, state: ParserState) -> IntLiteral:
        token = self._expect(TokenKind.INTEGER, "Expected integer literal.")
        lit: IntLiteral = IntLiteral(int(token.lexeme))
        self._set_expr_metadata(lit, token)
        return lit

    def _parse_float_literal(self, state: ParserState) -> FloatLiteral:
        token = self._expect(TokenKind.FLOAT, "Expected float literal.")
        lit: FloatLiteral = FloatLiteral(float(token.lexeme))
        self._set_expr_metadata(lit, token)
        return lit

    def _parse_string_literal(self, state: ParserState) -> StringLiteral:
        token = self._expect(TokenKind.STRING, "Expected string literal.")
        lit: StringLiteral = StringLiteral(token.lexeme)
        self._set_expr_metadata(lit, token)
        return lit

    def _parse_array_literal(
        self, state: ParserState
    ) -> Union[ObjectLiteral, NewArrayLiteral]:
        tobj = self._expect(TokenKind.ARRAY, "Expected 'array' keyword.")
        obj: ObjectLiteral
        if self._at().kind == TokenKind.SEMICOLON:
            return NewArrayLiteral(self._get_meta(tobj))
        else:
            obj = self._parse_array_literal_elements(state)
        self._set_expr_metadata(obj, tobj)
        obj.okind = ObjectKind.ARRAY
        return obj

    def _parse_array_literal_elements(self, state: ParserState) -> ObjectLiteral:
        self._expect(TokenKind.OPEN_BRACKET, "Expected '[' after array.")
        elements: list[IExpr] = []
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACKET:
            elements.append(self._parse_expr(state))
            if self._at().kind != TokenKind.CLOSE_BRACKET:
                self._expect(TokenKind.COMMA, "Expected ',' after array element.")
                if self._at().kind == TokenKind.CLOSE_BRACKET:
                    raise SyntaxError(
                        "Trailing comma in array literal is not allowed.",
                        self._get_curr_meta(),
                    )
        self._expect(TokenKind.CLOSE_BRACKET, "Expected ']' after array elements.")
        return ObjectLiteral(
            [PropertyLiteral(str(i), el) for i, el in enumerate(elements)]
        )

    def _parse_record_literal(
        self, state: ParserState
    ) -> Union[ObjectLiteral, NewRecordLiteral]:
        tobj = self._eat()  # eat 'record'
        objexpr: ObjectLiteral
        if self._at().kind == TokenKind.SEMICOLON:
            return NewRecordLiteral(self._get_meta(tobj))
        else:
            objexpr = self._parse_record_literal_elements(state)
        self._set_expr_metadata(objexpr, tobj)
        objexpr.okind = ObjectKind.RECORD
        return objexpr

    def _parse_record_literal_elements(self, state: ParserState) -> ObjectLiteral:
        self._expect(TokenKind.OPEN_BRACE, "Expected '{' after record.")
        properties: list[PropertyLiteral] = []
        while self._not_eof() and self._at().kind != TokenKind.CLOSE_BRACE:
            key = self._expect(TokenKind.STRING, "Expected string for record key.")
            self._expect(TokenKind.COLON, "Expected ':' after record key.")
            value = self._parse_expr(state)
            prop = PropertyLiteral(key.lexeme, value)
            self._set_expr_metadata(prop, key)
            properties.append(prop)
            # this allows for shorhand key, key -> { key, key, ... }
            if self._at().kind == TokenKind.COMMA:
                self._eat()  # eat ','
                if self._at().kind == TokenKind.CLOSE_BRACE:
                    raise SyntaxError(
                        "Trailing comma in record literal is not allowed.",
                        self._get_curr_meta(),
                    )
        self._expect(TokenKind.CLOSE_BRACE, "Expected '}' after object properties.")
        return ObjectLiteral(properties)

    # ----------------------------------------- Utility Functions -----------------------------------------

    def print(self, program: ProgramNode) -> None:
        print()
        print("AST:")
        try:
            print(json.dumps(program.json(True), indent=4))
        except Exception as e:
            print(e)
            print(program.json(True))
        print()  #
