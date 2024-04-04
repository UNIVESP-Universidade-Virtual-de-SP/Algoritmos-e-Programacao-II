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
