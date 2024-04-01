"""
Exercício 1
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
