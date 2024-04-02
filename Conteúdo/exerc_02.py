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
