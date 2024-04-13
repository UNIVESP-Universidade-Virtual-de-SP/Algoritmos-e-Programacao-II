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
### Exercício 10 📝
### Exercício 11 📝
### Exercício 12 📝
### Exercício 13 📝
### Exercício 14 📝
## Semana 3 ✅
## Semana 4 ✅
## Semana 5 ✅
## Semana 6 ✅
## Semana 7 ✅
