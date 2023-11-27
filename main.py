import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'IDENTIFIER'
)

# Reglas para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='

# Regla para identificadores (por ejemplo, nombres de variables)
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Regla para números flotantes
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

# Regla para ignorar espacios y tabulaciones
t_ignore = ' \t'

# Regla para manejar errores
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Reglas de precedencia
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),
)

# Diccionario para almacenar nombres de variables
names = {}

# Reglas de la gramática

# Regla para asignación
def p_statement_assign(p):
    'statement : IDENTIFIER EQUALS expression'
    names[p[1]] = p[3]
    p[0] = p[3]
    print(f"Asignación: {p[1]} = {p[3]}")

# Regla para expresiones
def p_statement_expr(p):
    'statement : expression'
    p[0] = p[1]
    print(f"Expresión evaluada: {p[1]}")

# Regla para operaciones binarias
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+': p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]
    print(f"Operación: {p[1]} {p[2]} {p[3]} = {p[0]}")

# Regla para negación unaria
def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]
    print(f"Negación unaria: -{p[2]} = {p[0]}")

# Regla para agrupación (paréntesis)
def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]
    print(f"Agrupación: ({p[2]})")

# Regla para números
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]
    print(f"Número: {p[1]}")

# Regla para nombres de variables
def p_expression_name(p):
    'expression : IDENTIFIER'
    try:
        p[0] = names[p[1]]
        print(f"Variable: {p[1]} = {p[0]}")
    except LookupError:
        print(f"Nombre indefinido '{p[1]}'")
        p[0] = 0

# Regla para manejar errores de sintaxis
def p_error(p):
    print("Error de sintaxis!")

# Construir el parser
parser = yacc.yacc(debug=True, write_tables=False)

# Función para probar el parser
def test_parser(input_string):
    result = parser.parse(input_string)
    if result is not None:
        print(f"Resultado final: {result}")

# Prueba con una cadena de entrada
input_string = input("Ingrese una expresión matemática: ")
test_parser(input_string)
