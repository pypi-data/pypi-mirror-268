# Macal DSL 6

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

2). In string interpolation you could technically embed strings in the expression part(s) (between {}), however, 
    these strings can't have the same string terminator as the string that they part of.
    
    This will not work:

    s = $"{a} : {b["a"]}";
    Error:

    Syntax Error: Expected ';' after variable declaration, got 'a'.
    Possible premature string termination, or the same termination was used in interpolation.
     at line 1 and column 17 in scripts/debug.mcl

    This will work:

    s = $"{a} : {b['a']}";

