from tkinter import *

wn = Tk()
wn.title("mi primer interfaz grafica en python")
wn.resizable(True,False) #poder agrandar o no el ancho y alto
wn.iconbitmap(r"C:\python\PYTHON\tkinter\img\pinguino.ico")
wn.geometry("500x500")
wn.config(bg="black")

marco=Frame()
marco.pack()
marco.config(bg="blue")
marco.config(width="140",height="140")
marco.config(relief="ridge",bd=10)

etiqueta= Label(text="hola mundo en tkinter", font=20)
etiqueta.pack()
etiqueta.config(bg="purple")
etiqueta.config(relief="sunken",bd=5)

etiqueta2= Label(text="#etiqueta dos#", font=18)
etiqueta2.place(x=190,y=200)
etiqueta2.config(bg="yellow")
etiqueta2.config(relief="sunken",bd=5)

imagentk=PhotoImage(file=r"C:\python\PYTHON\tkinter\img\tkinterlogo.png")

etiqueta3= Label(image=imagentk)
etiqueta3.place(x=150,y=250)
etiqueta3.config(bg="black")

wn.mainloop()