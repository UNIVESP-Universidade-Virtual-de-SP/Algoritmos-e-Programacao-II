"""
Problema Prático 10.2

Use o pensamento recursivo para implementar a função recursiva saúde() que, sobre a entrada inteira n, exibe n strings 'Hip ' seguidos por Hurrah.

>>> cheers(0)

Hurrah!!!

>>> cheers(1)

Hip Hurrah!!!

>>> cheers(4)

Hip Hip Hip Hip Hurrah!!!

O caso básico da recursão deverá ser quando n é 0; sua função deverão, então, exibir Hurrah. Quando n > 1, sua função deverá exibir 'Hip ' e depois chamar recursivamente a si mesma sobre a entrada inteira n – 1."""

def cheers(n:int=0):
    print(f"{'Hip ' * n}Hurrah!!!")

cheers(4)
