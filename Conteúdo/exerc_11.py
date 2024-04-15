"""
Implemente os operadores sobrecarregados len(), repr() e == para a classe Baralho. Sua nova classe Baralho deverá se comportar conforme mostramos:

>>> len(Baralho()))

52

>>> Baralho() == Baralho()

True

>>> Baralho() == eval(repr(Baralho()))

True
"""

from random import shuffle

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

class Baralho:
    'representa um baralho de 52 cartas'
    # valores e naipes são variáveis da classe Baralho
    # naipes são 4 símbolos Unicode representando os 4 naipes
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
    def __init__(self, valores:set={'2','3','4','5','6','7','8','9','10','J','Q','K','A'}):
        'inicializa baralho de 52 cartas'
        self.valores = valores
        self.baralho = []       # baralho está inicialmente vazio
        for naipe in Baralho.naipes: # naipes e valores são Baralho
            for valor in valores: # variáveis da classe 	
                # inclui Carta com certo valor e naipe no baralho   	
                self.baralho.append(Card(valor, naipe))    	
    def distribuiCarta():
        'distribui (remove e retorna) carta do topo do baralho'
        return self.baralho.pop()
    def shuffle(self):
        'mistura o baralho'
        shuffle(self.baralho)
    def show(self):
        'mistura o baralho'
        for i in self.baralho:
            print(i.valor, i.suit)
        print(len(self.baralho))
    def __len__(self):
        return len(self.baralho)
    def __repr__(self):
        return f"Baralho({self.valores})"
    def __eq__(self, other):
        try:
            return self.baralho == outro.baralho
        except Exception as e:
            return "Invalid use of =="

a = Baralho(valores={1,2,3,4,5})

b = repr(a)
