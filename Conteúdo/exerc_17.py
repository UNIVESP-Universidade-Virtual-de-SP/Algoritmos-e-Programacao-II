"""
No Capítulo 5, implementamos a função fatorial() iterativamente. A função fatorial n! tem uma definição recursiva natural:

n!   =                         1    se n = 0
                 n · (n− 1)!     se n > 0

Reimplemente a função fatorial() usando a recursão. Além disso, estime quantas chamadas à fatorial() são feitas para algum valor de entrada n > 0.
"""

def fatorial(n:int):
    i = 1
    while (n > 1):
        i *= n
        n-=1
    return i

print(fatorial(0))
