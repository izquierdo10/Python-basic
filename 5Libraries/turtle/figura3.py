from turtle import *

bgcolor("black")

pluma = Turtle()

pluma2 = Turtle()
pluma3 = Turtle()
pluma4 = Turtle()
pluma5 = Turtle()

x=0
while x<=3:
    color("blue")
    pensize(10)
    forward(200)
    left(90)
    x=x+1

z=0
pluma.goto(100,100)
while z<=3:
    pluma.color("blue")
    pluma.pensize(10)
    pluma.forward(200)
    pluma.left(90)
    z=z+1
#-----------------------
pluma2.goto(200,200)
pluma2.color("#01f6ff")
pluma2.pensize(10)
pluma2.left(45)
pluma2.forward(145)

pluma3.goto(200,0)
pluma3.color("#01f6ff")
pluma3.pensize(10)
pluma3.left(45)
pluma3.forward(145)
#----------------------
pluma4.goto(0,200)
pluma4.color("#01f6ff")
pluma4.pensize(10)
pluma4.left(45)
pluma4.forward(145)

pluma5.goto(0,0)
pluma5.color("#01f6ff")
pluma5.pensize(10)
pluma5.left(45)
pluma5.forward(145)


mainloop()





