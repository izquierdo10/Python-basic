from turtle import *
import random

bgcolor("black")

pluma = Turtle()
pluma2 = Turtle()
pluma3 = Turtle()

for x in range(100):

    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colormode(255)

    color(r,g,b)
    speed(30)
    circle(80+x)

    pluma.color(r,g,b)
    pluma.speed(30)
    pluma.setheading(180) # el metodo setheading mueve la direcion de la pluma
    pluma.circle(80+x)

    pluma2.color(r,g,b)
    pluma2.speed(30)
    pluma2.setheading(90)
    pluma2.circle(80+x)

    pluma3.color(r,g,b)
    pluma3.speed(30)
    pluma3.setheading(270)
    pluma3.circle(80+x)


mainloop()