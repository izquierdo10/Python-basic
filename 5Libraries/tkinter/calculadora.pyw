from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Calculadora")
raiz.resizable(False,False)
raiz.iconbitmap(r"C:\python\PYTHON\tkinter\img\logocalculadora.ico")
raiz.config(bg="black")

i=0 # posicion de espacio en el cuadro de texto
cont=0 # valor de uso de la funcion clicigual

#cuadro de texto--------------------------------------------------
pantalla = Entry(raiz,font=("calibri 20"),bg="white",width=24)
pantalla.grid(row=0,column=0, columnspan=5)

#Funciones--------------------------------------------------------
def clicBoton(valor): # valores 
    global i,cont
    if cont>0:# si se uso la funcion clicIgual borre primer el resultado y ahi si ingrese los nuevos datos
        pantalla.delete(i,END)
        pantalla.insert(i,valor)
        i=i+1
    else:# ingrese los datos 
        pantalla.insert(i,valor)
        i=i+1

def borrarTodo(): # borrar todos lo caracteres
    pantalla.delete(0,END)
    global i
    i=0

def borrar(): # borrar caracter uno a uno en decremento
    global i
    if i>0: #correcion al borrar el resultado
        pantalla.delete(i-1)
        i=i-1
    else: 
        pantalla.delete(0,END)

def clicIgual():
    try:# control de error
        caracteres=pantalla.get() #llamamos los datos en pantalla y los guardamos
        resultado=eval(caracteres)# el metodo eval nos permite operar los caracteres de forma matematica 
        borrarTodo()
        pantalla.insert(0,resultado)
        global cont
        cont=cont+1# registro de uso de la funcion
    except Exception as E: # si da error entonces......
        error="Error de Sintaxis"
        borrarTodo()
        pantalla.insert(0,error)
        cont=cont+1

#estilo de los botones-------------------------------------------------------
estilo_botones =ttk.Style()
estilo_botones.configure('botones.TButton',font="arial 15",width=5, relief="flat",background="#008073")

#botones numeros--------------------------------------------------------------
boton0 = ttk.Button(raiz, text="0",style="botones.TButton",command=lambda: clicBoton(0))
boton1 = ttk.Button(raiz, text="1",style="botones.TButton",command=lambda: clicBoton(1))
boton2 = ttk.Button(raiz, text="2",style="botones.TButton",command=lambda: clicBoton(2))
boton3 = ttk.Button(raiz, text="3",style="botones.TButton",command=lambda: clicBoton(3))
boton4 = ttk.Button(raiz, text="4",style="botones.TButton",command=lambda: clicBoton(4))
boton5 = ttk.Button(raiz, text="5",style="botones.TButton",command=lambda: clicBoton(5))
boton6 = ttk.Button(raiz, text="6",style="botones.TButton",command=lambda: clicBoton(6))
boton7 = ttk.Button(raiz, text="7",style="botones.TButton",command=lambda: clicBoton(7))
boton8 = ttk.Button(raiz, text="8",style="botones.TButton",command=lambda: clicBoton(8))
boton9 = ttk.Button(raiz, text="9",style="botones.TButton",command=lambda: clicBoton(9))

boton9.grid(row=1,column=2, padx=1)
boton8.grid(row=1,column=1, padx=1)
boton7.grid(row=1,column=0, padx=1)
boton6.grid(row=2,column=2, padx=1, pady=2)
boton5.grid(row=2,column=1, padx=1, pady=2)
boton4.grid(row=2,column=0, padx=1, pady=2)
boton3.grid(row=3,column=2, padx=1, pady=2)
boton2.grid(row=3,column=1, padx=1, pady=2)
boton1.grid(row=3,column=0, padx=1, pady=2)
boton0.grid(row=4,column=1, padx=1, pady=2)
#botones operaciones aritmeticas-------------------------------------------------
botonMul = ttk.Button(raiz, text="x",style="botones.TButton",command=lambda: clicBoton("*"))
botonDiv = ttk.Button(raiz, text="/",style="botones.TButton",command=lambda: clicBoton("/"))
botonSum = ttk.Button(raiz, text="+",style="botones.TButton",command=lambda: clicBoton("+"))
botonRes = ttk.Button(raiz, text="-",style="botones.TButton",command=lambda: clicBoton("-"))

botonMul.grid(row=2,column=3, padx=1, pady=2)
botonDiv.grid(row=2,column=4, padx=1, pady=2)
botonSum.grid(row=3,column=3, padx=1, pady=2)
botonRes.grid(row=3,column=4, padx=1, pady=2)

#botones borrado------------------------------------------------------------------
botonDEL  = ttk.Button(raiz, text="⌫",style="botones.TButton",command=lambda: borrar())
botonAC = ttk.Button(raiz,text="AC",style="botones.TButton",command=lambda: borrarTodo())

botonDEL.grid(row=1,column=3, padx=1)
botonAC.grid(row=1,column=4, padx=1)
#boton igual y coma ----------------------------------------------
bontonIgual = ttk.Button(raiz, text="=" ,style="botones.TButton",command=lambda: clicIgual())
bontonComa  = ttk.Button(raiz, text="." , style="botones.TButton",command=lambda: clicBoton("."))

bontonIgual.grid(row=4,column=3,columnspan=2,padx=1, pady=2, sticky=(W,E))
bontonComa.grid(row=4,column=0,padx=1, pady=2)

raiz.mainloop()