"""
Implemente operadores sobrecarregados repr() e == para a classe Card. Sua nova classe Card deverá se comportar como a seguir:

>>> Card('3', '♠') == Card('3', '♠')

True

>>> Card('3', '♠') == eval(repr(Card('3', '♠')))

True
"""

class Card:
    'representa uma Card do jogo'
    def __init__(self, value:str, naipe:str):
        'inicializa valor e naipe da Card do jogo'
        self.value = value
        self.suit = naipe
    def getRank(self):
        'retorna valor'
        return self.valor
    def getSuit(self):
        'retorna naipe'
        return self.naipe
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit
    def __repr__(self):
        return f"Card('{self.value}', '{self.suit}')"

print(Card('3', '♠') == Card('3', '♠'))
print(Card('3', '♠') == eval(repr(Card('3', '♠'))))
