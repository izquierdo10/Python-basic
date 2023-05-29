from turtle import *
import random

bgcolor("black")

pluma = Turtle()
pluma2= Turtle()
#----------------------------
def colores(): # funcion de colores rgb
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colormode(255)
    return (r,g,b)
#----------------------------
x=0
y=0
while x<50:#centro
    color(colores())
    speed(30)
    circle(100)
    setheading(10+y) # valla moviendo el circulo sigiente 10 grados mas
    y=y+10
    x+=1

#----------------------------
pluma.goto(0,-200)
for i in range(50):#circulo
    pluma.color(colores())
    pluma.speed(30)
    pluma.circle(200+i) # aumente el tamaño del circulo +1
    pluma.goto(0,-200-i) # aumente el punto de partida del circulo

#----------------------------

mainloop()


