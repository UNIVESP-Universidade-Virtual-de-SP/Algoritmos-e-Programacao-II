"""
Implemente o método recursivo pattern2(), que aceita um inteiro não negativo como entrada e exibe o padrão mostrado a seguir. Os padrões para as entradas 0 e 1 são nada e um asterisco, respectivamente:
"""
def pattern(n):
    'exibe o enésimo padrão'
    if n == 0:           # caso básico
        print("*" * 0, end=' ')
    else:                # etapa recursiva: n > 0
        pattern(n-1)         # exibe padrão n-1
        print("*" * n, end='\n')    # exibe n
        pattern(n-1)         # exibe padrão n-1

def pattern2(n):
    pattern(n)

pattern(2)
