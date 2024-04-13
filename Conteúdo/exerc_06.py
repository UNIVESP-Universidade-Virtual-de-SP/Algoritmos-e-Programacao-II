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
