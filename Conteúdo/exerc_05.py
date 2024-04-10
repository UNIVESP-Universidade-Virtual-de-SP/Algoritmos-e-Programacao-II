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
