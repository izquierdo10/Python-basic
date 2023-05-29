from turtle import * # importamos la libreria turtle para hacer graficos vectoriales

#ventana
title("PlayStation")
bgcolor("black")

pluma = Turtle() #creamos el objeto que va hacer uso del grafico
for c in range(4):#cuadrado
    pluma.pensize(5)
    pluma.color("#c239c4")
    pluma.forward(100)
    pluma.left(90)

#circulo
pluma2 = Turtle()
pluma2.penup()
pluma2.setpos(200,0)
pluma2.pendown()
pluma2.pensize(5)
pluma2.color("#ff0000")
pluma2.circle(55)

#triangulo
pluma3 = Turtle()
pluma3.penup()
pluma3.setpos(-150,0)
pluma3.pendown()
for t in range(3):
    pluma3.pensize(5)
    pluma3.color("#83ff03")
    pluma3.forward(110)
    pluma3.left(120)

#equis
pluma4 = Turtle()
pluma4.penup()
pluma4.goto(-250, 50)
pluma4.pendown()

pluma4.pensize(5)
pluma4.color("#0169ff")

pluma4.left(45)# primera linea
pluma4.forward(70)

for x in range(3): # 2,3 y 4 linea
    pluma4.backward(70)

    pluma4.left(90)
    pluma4.forward(70)

mainloop()



















