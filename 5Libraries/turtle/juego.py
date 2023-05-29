from turtle import *
import random

#ventana
bgcolor("black")
title("juego propio")
setup(600,600 ,startx=100, starty=10)
#puntaje
score=Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.color("white")
score.goto(0,260)

#pluma
color("white")
penup()
shape("square")
goto(0,0)
speed(0)
#cuerpo_serpiente
cuerpo = []

#funcion direccion
def derecha():
    setheading(0)
def izquierda():
    setheading(180)
def arriba():
    setheading(90)
def abajo():
    setheading(270)
#asignamos las funciones a las teclas
onkey(derecha, "Right")
onkey(izquierda, "Left")
onkey(arriba, "Up")
onkey(abajo, "Down")
listen()#escuchamos en tiempo real el teclado

#funcion de movimiento
def mover():
#colicion con borde 
    x, y = position()
    if abs(x) > 280 or abs(y) > 280:
        def GG():
            bye()

    else:
        forward(20)
#colisión CUERPO
    for segmento in cuerpo[2:]: # Itera sobre todos los segmentos excepto el primero
        if distance(segmento) < 20: # Comprueba si la distancia es menor a 20
            return bye()
#colicion COMIDA
    if distance(comida)< 20:
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        comida.goto(x,y)
#creacion de cada segmento de la cola
        cola = Turtle()
        cola.speed(0)
        cola.color("grey")
        cola.penup()
        cola.shape("square")
        cuerpo.append(cola)#agregamos la cola a la matriz cuerpo 

    ontimer(mover, 100) # el metodo ontimer es para llamar la funcion en un determinado tiempo
#--------------------------------------------------
#movimiento del cuerpo
def MovCuerpo():
    totalcola=len(cuerpo)
    tracer(False)
    for i in range(0,totalcola,1):#segundo y demas segmentos pasan por el for
        x=cuerpo[i-i].xcor()
        y=cuerpo[i-i].ycor()
        cuerpo[i].goto(x,y)

    if totalcola>0:#primer segmento
        x=xcor()
        y=ycor()
        cuerpo[0].goto(x,y)

    score.clear()
    score.write("Score: {}".format(totalcola),align="center",
                font=("Courier",24,"normal")) 

    tracer(True)
    ontimer(MovCuerpo, 100)
#--------------------------------------------------
#comida
comida= Turtle()
comida.speed(0)
comida.shape("square")
comida.color("red")
comida.penup()
comida.goto(0,100)
#---------------------------------------------------

MovCuerpo()
mover()
mainloop() 
