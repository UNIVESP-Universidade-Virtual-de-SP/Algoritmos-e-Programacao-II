"""
Modifique o construtor da classe Baralho de modo que a classe também possa ser usada para jogos de carta que não usam o baralho padrão de 52 cartas. Para esses jogos, precisaríamos oferecer a lista de cartas explicitamente no construtor. Veja a seguir um exemplo um tanto artificial:
"""

class Card:
    'representa uma carta do jogo'
    def __init__(self, valor:str, naipe:str):
        'inicializa valor e naipe da carta do jogo'
        self.valor = valor
        self.suit = naipe
    def getRank(self):
        'retorna valor'
        return self.valor
    def getSuit(self):
        'retorna naipe'
        return self.naipe

from random import shuffle
class Baralho:
    'representa um baralho de 52 cartas'
    # valores e naipes são variáveis da classe Baralho
    valores = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}
    # naipes são 4 símbolos Unicode representando os 4 naipes
    naipes = {'\u2660', '\u2661', '\u2662', '\u2663'}
    def __init__(self, valores:set=valores):
        'inicializa baralho de 52 cartas'
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
        'MOstra as cartas no baralho'
        for i in self.baralho:
            print(i.valor, i.suit)
        print(len(self.baralho))
