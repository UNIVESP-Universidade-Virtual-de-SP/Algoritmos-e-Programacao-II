"""
Problema Prático 8.8

Implemente a classe Vetor, que aceita os mesmos métodos da classe Ponto que desenvolvemos na Seção 8.4. A classe Vetor também deverá aceitar a adição de vetor e operações de produto. A adição de dois vetores

>>> v1 = Vetor(1, 3)

>>> v2 = Vetor(-2, 4)

é um novo vetor cujas coordenadas são a soma das coordenadas correspondentes de v1 e v2:

>>> v1 + v2

Vetor(-1, 7)

O produto de v1 e v2 é a soma dos produtos das coordenadas correspondentes:

>>> v1 * v2

10

Para que um objeto Vetor seja exibido como Vetor (. , .) em vez de Ponto(. , .), você precisará redefinir o método _ _repr_ _().
"""

class Vetor:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vetor(x=(self.x + other.x), y=(self.y + other.y))
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    def __repr__(self):
        return f"Vetor({self.x}, {self.y})" 

v1 = Vetor(1, 3)
v2 = Vetor(-2, 4)
print(v1 + v2)
print(v1 * v2)

