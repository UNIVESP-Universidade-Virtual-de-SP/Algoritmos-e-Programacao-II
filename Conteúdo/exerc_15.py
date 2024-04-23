"""
Implemente o método recursivo reverse(), que aceita um inteiro não negativo como entrada e exibe os dígitos de n verticalmente, começando com o dígito de ordem baixa.
"""

def vertical(n:int):
    for i in range(len(str(n))):
        print(str(n)[i])

vertical(3125) # >>> 3 \n 1 \n 2 \n 5 \n  
