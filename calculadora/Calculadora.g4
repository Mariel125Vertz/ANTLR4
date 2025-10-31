grammar Calculadora;

// Reglas del Parser
prog: stat+ ;

stat
    : ID '=' expr NEWLINE                       # Assign
    | condicional                               # Conditional
    | expr NEWLINE                              # PrintExpr
    | NEWLINE                                   # Blank
    ;

condicional
    : 'if' '(' expr ')' bloque                  # IfStatement
    ;

bloque
    : '{' stat+ '}'                             # Block
    ;

expr
    : expr ('*'|'/') expr                       # MulDiv
    | expr ('+'|'-') expr                       # AddSub
    | expr (EQ | NE | LT | GT | LE | GE) expr   # Comparison
    | '(' expr ')'                              # Parens
    | ID                                        # Id
    | NUM                                       # Num
    ;

// Reglas del Lexer
ID: [a-zA-Z]+ ;
NUM: [0-9]+ ('.' [0-9]+)? ;
NEWLINE: '\r'? '\n' ;

EQ: '==';
NE: '!=';
LT: '<';
GT: '>';
LE: '<=';
GE: '>=';

WS: [ \t]+ -> skip ;
