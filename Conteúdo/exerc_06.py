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
