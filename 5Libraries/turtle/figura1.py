from turtle import *
import random

title("mandala")
bgcolor("black")

pluma = Turtle()

for i in range(400):

    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colormode(255) # con este metodo se establece el rango de colores que va a tener la pluma

    pluma.speed(30)
    pluma.color(r,g,b)
    pluma.forward(5+i)
    pluma.left(91)

mainloop()

