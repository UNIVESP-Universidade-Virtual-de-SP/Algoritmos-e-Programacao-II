"""
Modifique a classe Animal que desenvolvemos na seção anterior de modo que aceite um construtor com dois, um ou nenhum argumento de entrada:

>>> snoopy = Animal('cão', 'latir')

>>> snoopy.fala()

Eu sou um cão e sei latir.

>>> tweety = Animal('canário')

>>> tweety.fala()

Eu sou um canário e sei emitir sons.

>>> animal = Animal()

>>> animal.fala()

Eu sou um animal e sei emitir sons.
"""
class Animal:
    def __init__(self, name:str="animal", action:str="emitir sons") -> None:
        self.name = name
        self.action = action
    def action(self):
        ' exibe uma sentença pelo animal'
        print(f'Eu sou um {self.name} e sei {self.action}')

snoopy = Animal('cão', 'latir')
snoopy.fala()

tweety = Animal('canario')
tweety.fala()

animal = Animal()
animal.fala()
