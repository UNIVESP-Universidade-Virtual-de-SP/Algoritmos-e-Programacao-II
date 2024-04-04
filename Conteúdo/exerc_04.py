"""
>>> if x == 5
SyntaxError: invalid syntax

>>> print 'hello'
SyntaxError: invalid syntax

>>> lst = [4;5;6]
SyntaxError: invalid syntax

>>> for i in range(10):
print(i)

SyntaxError: expected an indented block

Em cada uma dessas instruções, o erro se deve a uma sintaxe (formato)
incorreta de uma instrução Python. Assim, esses erros ocorrem antes que o Python tenha 
sequer uma chance de executar a instrução sobre os argumentos dados, se houver.

Explique o que causa o erro de sintaxe em cada instrução listada anteriormente.
Depois, escreva uma versão correta de cada instrução Python.
"""

"""
if x == 5

SyntaxError: invalid syntax
Falta o ':'
"""
x = 5
if (x == 5):
    print("Sem Erros")

"""
>>> print 'hello'
SyntaxError: invalid syntax
Faltam parênteses
"""
print('hello')

"""
>>> lst = [4;5;6]
SyntaxError: invalid syntax
Os ';' devem ser trocados para ','
"""
lst = [4,5,6]
"""
>>> for i in range(10):
print(i)

Erro de Indentação
"""

for i in range(10):
    print(i)

l = [3, 4, (2, 1)] 
print(l[0])
print(l[2])
print(l[2][0])
print(l[-1][0])
