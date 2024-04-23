[Voltar ao ínicio ⬅️](/Algoritmos-e-Programacao-II/)

# Conteúdo 📚.

## Indíce

- [Semana 1 ✅.](#semana-1-)
    - [Exercício 01 📝](#exercício-01-)
    - [Exercício 02 📝](#exercício-02-)
    - [Exercício 03 📝](#exercício-03-)
    - [Exercício 04 📝](#exercício-04-)
- [Semana 2 ✅.](#semana-2-)
    - [Exercício 05 📝](#exercício-05-)
    - [Exercício 06 📝](#exercício-06-)
    - [Exercício 07 📝](#exercício-07-)
    - [Exercício 08 📝](#exercício-08-)
    - [Exercício 09 📝](#exercício-09-)
    - [Exercício 10 📝](#exercício-10-) 
    - [Exercício 11 📝](#exercício-11-)
    - [Exercício 12 📝](#exercício-12-)
    - [Exercício 13 📝](#exercício-13-)
    - [Exercício 14 📝](#exercício-14-) 
- [Semana 3 ✅.](#semana-3-)
- [Semana 4 ✅.](#semana-4-)
- [Semana 5 ✅.](#semana-5-)
- [Semana 6 ✅.](#semana-6-)
- [Semana 7 ✅.](#semana-7-)

## Semana 1 ✅
### Exercício 01 📝

Desenhar a símbolo das olimpíadas.

```python
"""
Implemente a função olimpíadas(t), que faz com que a tartaruga t
desenhe os anéis olímpicos mostrados a seguir. Use a função jump()
do módulo ch3. Você conseguirá obter a imagem desenhada executando:

"""
import turtle

s = turtle.Screen()
t = turtle.Turtle(visible=False)
t.pensize(5)

def olimpíadas(turtle, screen):
    def drawCircle(radius:int, x:float, y:float, color:str):
        turtle.color(color)
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.circle(radius)
    drawCircle(50, x=screen.window_width() * 0.08, y=0, color="#0F0")
    drawCircle(50, x=screen.window_width() * -0.08, y=0, color="#FF0")
    drawCircle(50, x=0, y=screen.window_height() * 0.1, color="#000")
    drawCircle(50, x=screen.window_width() * 0.17, y=screen.window_height() * 0.1, color="#F00")
    drawCircle(50, x=screen.window_width() * -0.17, y=screen.window_height() * 0.1, color="#00F")
    screen.mainloop()

olimpíadas(t, s)
```

### Exercício 02 📝
```python
"""
Problema Prático 4.8

Escreva a função palavras() que aceita um argumento de entrada — um nome de arquivo — e retorna a lista de palavras 
reais (sem símbolos de pontuação !,.:;?) no arquivo.

>>> palavras('example.txt')

['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with',

 'the', 'new', 'line', 'character', 'There', 'is', 'a',

 'blank', 'line', 'above', 'this', 'line']
"""

def palavras(fileName=str):
    file = open(fileName, "r")
    fileWords = file.read().translate(str.maketrans(".?,:;!", "      "))
    print(fileWords.split())
```

### Exercício 03 📝

```python
"""
Implemente a função meuGrep(), que toma como entrada duas strings, um nome de arquivo e uma string alvo, e exibe cada linha do arquivo que contém a string alvo como uma substring.

>>> exerc_02('example.txt', 'line')

The 3 lines in this file end with the new line character.

There is a blank line above this line.
"""   

def meuGrep(file=str, alvo=str):
    targetFile = open(file, "r")
    for linha in targetFile.readlines():
        if alvo.lower() in linha.lower():
            print(linha) 

meuGrep("testForFun.txt", "lorem") 
```

### Exercício 04 📝
```python
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
```

## Semana 2 ✅

### Exercício 05 📝
```python
"""
    Acrescente o método getx() à classe Ponto; esse método não aceita entrada e retorna a coordenada x do objeto Ponto que chama o método.
"""

class Point:
    'classe que representa pontos no plano'
    def setx(self, coordx):
        'define coordenada x do ponto como coordx'
        self.x = coordx
    def sety(self, coordy):
        'define coordenada y do ponto como coordy'
        self.y = coordy
    def getx(self, coordx):
        'define coordenada x do ponto como coordx'
        return self.x
    def get(self):
        'retorna tupla com coordenadas x e y do ponto'
        return (self.x, self.y)
    def move(self, dx, dy):
        'muda as coordenadas x e y por dx e dy'
        self.x += dx
        self.y += dy
```
### Exercício 06 📝
```python
"""
A classe Teste tem apenas um atributo, a variável de classe version, que se refere ao valor float 1.02.
(a) Desenhe os namespaces associados à classe e aos dois objetos, os nomes – se houver – neles contidos e os valores aos quais os nomes se referem.
(b) Execute essas instruções e preencha os pontos de interrogação:

a.version
b.version
Teste.version

Teste.version=1.03
a.version
Ponto.version

a.version = 'Última!!'
Ponto.version
b.version
a.version

c) Desenhe o estado dos namespaces após essa execução. Explique por que as três últimas expressões são avaliadas dessa forma.
"""

class Teste:
    version = 1.02

a = Teste()
b = Teste()

a.version # >>> 1.02
b.version # >>> 1.02
Teste.version # >>> 1.02
Teste.version = 1.03 # >>> 1.03
a.version # >>> 1.03
a.version = 'Última!!' # version >> "Última"
b.version # >>> 1.03
a.version # >>> "Última"
```
### Exercício 07 📝
```python
"""
    Implemente a classe Retângulo, que representa retângulos. A classe deverá implementar estes métodos:
"""
class Retangulo:
    def setTamanho(self, width:int, height:int):
        self.width = width 
        self.height = height 
    def perimetro(self):
        return 2*(self.width + self.height)
    def area(self):
        return (self.width * self.height)
```
### Exercício 08 📝
```python

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
```
### Exercício 09 📝
```python
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
        'mistura o baralho'
        for i in self.baralho:
            print(i.valor, i.suit)
        print(len(self.baralho))
```

### Exercício 10 📝

```python
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
```
### Exercício 11 📝
```python
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
```

### Exercício 12 📝
```python
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
```
### Exercício 13 📝
```python
"""
Reimplemente o método dequeue() da classe Queue de modo que seja levantada uma exceção KeyboardInterrupt (um tipo de exceção impróprio, nesse caso) com a mensagem 'remoção de uma fila vazia ' (uma mensagem de erro realmente apropriada) se for feita uma tentativa de remover algum elemento de uma fila vazia.

>>> queue = Queue()

>>> queue.dequeue()

Traceback (most recent call last):

  File "<pyshell#30>", line 1, in <module>

    queue.dequeue()

  File "/Users/me/ch8.py", line 183, in dequeue

    raise KeyboardInterrupt('remoção de uma fila vazia')

KeyboardInterrupt: remoção de uma fila vazia
"""
class Queue:
    'uma classe de fila clássica'
    def __init__(self):
        'instancia uma lista vazia'
        self.q = []
    def isEmpty(self):
        'retorna True se a fila estiver vazia, False caso contrário'
        return (len(self.q) == 0)
    def enqueue (self, item):
        'Insere item no final da fila'
        return self.q.append(item)
    def dequeue(self):
        if (len(self.q) == 0):
            raise KeyboardInterrupt("Remoção de uma fila vazia")
        return self.q.pop(0)

v1 = Queue()
v1.dequeue()
```
### Exercício 14 📝
```
Problema Prático 8.10

Lembre-se de que também podemos percorrer um contêiner Queue usando o padrão de laço contador (isto é, percorrendo os índices).

>>> for i in range(len(q)):
         print(q[i])
>>> 3
>>> 5
>>> 7
>>> 9
Que operador sobrecarregado, além do operador de indexação, precisa ser implementado para poder percorrer um contêiner usando esse padrão?
```
Resposta: len()

## Semana 3 ✅
```python
"""
Implemente o método recursivo reverse(), que aceita um inteiro não negativo como entrada e exibe os dígitos de n verticalmente, começando com o dígito de ordem baixa.
"""

def vertical(n:int):
    for i in range(len(str(n))):
        print(str(n)[i])
vertical(3125) # >>> 3 \n 1 \n 2 \n 5 \n
```
## Semana 4 ✅
## Semana 5 ✅
## Semana 6 ✅
## Semana 7 ✅
