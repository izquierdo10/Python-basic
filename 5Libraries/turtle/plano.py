import turtle

pixeles=int(input("en cuantos pixeles deseas trasar los puntos:"))

ventana = turtle.Screen()
ventana.bgcolor("black")
ventana.title("plano cartesiano")
# obtiene las dimensiones de la ventana predeterminada
ancho = ventana.window_width()
alto = ventana.window_height()

divAncho=int(ancho/2)
divAlto=int(alto/2)
#----------------------------------------------------------------
lineaY = turtle.Turtle()
lineaY.color("purple")
lineaY.setheading(90)
lineaY.forward(divAlto)
lineaY.backward(alto)
lineaY.hideturtle()

puntosY = turtle.Turtle()
puntosY.color("blue")
puntosY.pensize(10)
puntosY.speed(30)

lineaPY=turtle.Turtle()
lineaPY.color("white")
lineaPY.speed(30)


for po in range(0,divAlto,pixeles):
    puntosY.penup()
    puntosY.goto(0,po)
    puntosY.pendown()
    puntosY.goto(0,po)
#######################
    lineaPY.penup()
    lineaPY.goto(10,po)
    lineaPY.pendown()
    lineaPY.forward(divAncho)
    lineaPY.backward(ancho)

for ne in range(0,divAlto,pixeles):
    puntosY.penup()
    puntosY.goto(0,-ne)
    puntosY.pendown()
    puntosY.goto(0,-ne)
#######################
    lineaPY.penup()
    lineaPY.goto(10,-ne)
    lineaPY.pendown()
    lineaPY.forward(divAncho)
    lineaPY.backward(ancho)

puntosY.hideturtle()
#----------------------------------------------------------------
lineaX = turtle.Turtle()
lineaX.color("purple")
lineaX.forward(divAncho)
lineaX.backward(ancho)
lineaX.hideturtle()


puntosX = turtle.Turtle()
puntosX.color("blue")
puntosX.pensize(10)
puntosX.speed(30)

lineaPX=turtle.Turtle()
lineaPX.color("white")
lineaPX.setheading(90)
lineaPX.speed(30)


for po in range(pixeles,divAncho,pixeles):
    puntosX.penup()
    puntosX.goto(po,0)
    puntosX.pendown()
    puntosX.goto(po,0)
#######################
    lineaPX.penup()
    lineaPX.goto(po,10)
    lineaPX.pendown()
    lineaPX.forward(divAlto)
    lineaPX.backward(alto)

for ne in range(pixeles,divAncho,pixeles):
    puntosX.penup()
    puntosX.goto(-ne,0)
    puntosX.pendown()
    puntosX.goto(-ne,0)
#######################
    lineaPX.penup()
    lineaPX.goto(-ne,10)
    lineaPX.pendown()
    lineaPX.forward(divAlto)
    lineaPX.backward(alto)

puntosX.hideturtle()
lineaPX.hideturtle()
lineaPY.hideturtle()

#----------------------------------------------------------------
def print_coordinates(x, y):
    turtle.onscreenclick(None)  # desactiva temporariamente el evento click para evitar recursividad
    turtle.clear()             # borra la pantalla antes de mostrar las nuevas coordenadas
    turtle.goto(x, y)  # mueve la tortuga a la posición del clic
    turtle.color("white")
    turtle.penup()          
    turtle.write("Coordenadas: (X:{},Y:{})".format(x,y), align="center", font=("Arial", 16, "normal"))
    turtle.onscreenclick(print_coordinates)  # reactiva el evento click

turtle.speed(0)                 # desactiva la animación para una respuesta más rápida
turtle.onscreenclick(print_coordinates)  # activa el evento click

# imprime las dimensiones de la ventana predeterminada
print("Ancho predeterminado:", ancho)
print("Alto predeterminado:", alto)

turtle.done()