# Macal DSL 5.5 Alpha 2

## Introduction

This is version 5.5 of the Macal DSL language
This is an interim version.

I have removed the bytecode compiler and runtime.
Version 5.5 is to fix several problems in regards to scope and the way functions were implemented.
Version 6.0 will use llvmlite and jit compilation.

Known issues:
1).  If you include a file for which there are multiple files in the file search path that have the same file name, 
     there is no way of telling which one gets included.
     A safeguard is in place to prevent importing a file from itself, but i can't exclude multiple files with
     the same name on the search path other than the user controlling the search path.

## Installation

```bash
python3 -m pip install macal==5.5.0.alpha.2
```

## Usage

Macal can be used in 3 main ways:

1). Use it on the commandline with 'mrepl' to run interactively.

2). Use it on the commandline with 'mrun' to run a file. (type mrun -h to get help).

3). Include the class in your product and work from there.
    An example will be provided in a later chapter.


## Instruction set "EBNF"


letter = "a".."z" | "A".."Z"

digit = "0".."9"

ident = letter | "_" | digit

stmt = return_stmt | continue_stmt | break_stmt | halt_stmt | if_stmt | while_stmt | foreach_stmt | switch_stmt |
       include_stmt | select_stmt | functiondefinition_stmt | external_stmt | vardeclaration_stmt | functioncall_stmt | builtin_functions

builtin_functions = print_stmt | is_type_stmt | type_stmt
is_type_stmt = isrecord_stmt | isarray_stmt | isstring_stmt | isint_stmt | isfloat_stmt | isbool_stmt | isnil_stmt |
               isfunction_stmt | isobject_stmt

return_stmt = "return" [ expr ] ";"

continue_stmt = "continue" ";"

break_stmt = "break" ";"

halt_stmt = "halt" [ expr ] ";"

if_stmt = "if" expr "{" stmt... "}" [ "elif" expr "{" stmt... "}" ... ] [ "else" "{" stmt... "}" ]

while_stmt = "while" expr "{" stmt... "}"

foreach_stmt = "foreach" expr "{" stmt... "}"

switch_stmt = "switch" expr "{" case_stmt... [ default_stmt ] "}"

case_stmt = "case" expr ":" "{" stmt... "}"

default_stmt = "default" ":" "{" stmt... "}"

include_stmt = "include" lib_name [ "," lib_name... ] ";"

select_stmt = "select" [ "distinct" ] field_list "from" expr [ "where" expr ] [ "merge" ] "into" expr ";"

lib_name = ident

field_list = field ([ "," field ])*

field = field_name [ "as" alias ]

field_name = ident

functioncall_stmt = ident "(" expr ["," expr]... ")" ";"

functiondefinition_stmt = ident "=>" "(" [ ident [ "," ident ]... ] ")" "{" stmt... "}"

external_stmt = ident "=>" "(" [ ident [ "," ident ]... ] ")" "external" python_module "," external_function_name

python_module = string_literal

external_function_name = string_literal

vardeclaration_stmt = ident "=" ([ident "="])* expr ";"

isrecord_stmt = isRecord( expr ) ";"

isarray_stmt = isArray( expr ) ";"

isstring_stmt = isString( expr ) ";"

isint_stmt = isInt( expr ) ";"

isfloat_stmt = isFloat( expr ) ";"

isbool_stmt = isBool( expr ) ";"

isnil_stmt = isNil( expr ) ";"

isfunction_stmt = isFunction( expr ) ";"

isobject_stmt = isObject( expr ) ";" ;

type_stmt = "type" "(" expr ")" ";"

print_stmt = "print" "(" expr ([, expr])* ")" ";"

array_variable = ident "[" expression "]"

record_variable = ident ({ "." ident | "[" string_literal "]" })*

string_literal = '"' literal '"'

expr = assignment_expr

assignment_expr = string_concatenation ( "=" | "+=" | "-=" | "*=" | "/=" | "%=" | "^=" | ".=" ) assignment_expr

string_concatenation = object_expr ( "+." ) object_expr

object_expr = object "{" ident ":" expr ([ "," ident ":" expr ])* "}" | array_expr

array_expr = "[" expr (["," expr])* "]"

record_expr = "{" expr (["," expr])* "}"

logical_expr = comparison_expr ("and", "or", "xor", "&&", "||") comparison_expr

comparison_expr = addition_expr ({"<", "<=", ">", ">=", "==", "!="}) addition_expr

addition_expr = multiplication_expr ("+", "-") multiplication_expr

multiplication_expr = power_expr ("*", "/", "%") power_expr

power_expr = unary_expr ("^") unary_expr

unary_expr = ("-", "++", "--") unary_expr | call_member_expr

call_member_expr = member_expr | "(" call_expr

call_expr = args "(" call_expr(callee)

args = "(" arg_list ")"

arg_list = expr (",") expr

member_expr = primary_expr ("." primary_expr | "[" "]" new array_element | "[" expr "]") 

new_array_element = "=" expr

primary_expr = ident | int_number | float_number | string_literal | "(" expr ")" | array_literal | record_literal |
               type_stmt | is_type_stmt
