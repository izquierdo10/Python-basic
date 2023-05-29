from tkinter import *

raiz = Tk()

marco=Frame(raiz,width=600, height=600)
marco.config(relief="solid", bd=2)
marco.pack()

#entradas
entrada=Entry(marco, width=30 )
entrada.grid(row=0, column=1 , padx=5, pady=5,sticky="w")

entrada2=Entry(marco, width=30 )
entrada2.grid(row=1, column=1 , padx=5, pady=5,sticky="w")

entrada3=Entry(marco, width=30 )
entrada3.grid(row=2, column=1 , padx=5, pady=5,sticky="w")

entrada4=Entry(marco, width=30 )
entrada4.grid(row=3, column=1 , padx=5, pady=5,sticky="w")
entrada4.config(show="♣")

entrada5=Text(marco, width=40 ,height=5)
entrada5.grid(row=4, column=1 , padx=5, pady=10)
#---------------------------------------------------------
#etiquetas
nombrelabel=Label(marco,text="Nombres:")
nombrelabel.grid(row=0, column=0 , padx=5, pady=5)

apellidolabel=Label(marco,text="Apellidos:")
apellidolabel.grid(row=1, column=0 , padx=5, pady=5)

celularlabel=Label(marco,text="Celular:")
celularlabel.grid(row=2, column=0 , padx=5, pady=5)

passlabel=Label(marco,text="Password:")
passlabel.grid(row=3, column=0 , padx=5, pady=5)

comentario=Label(marco, text="Comentarios:")
comentario.grid(row=4 , column=0, padx=5 , pady=10)
#---------------------------------------------------------
#escrol
scrolvert=Scrollbar(marco, command=entrada5.yview)
scrolvert.grid(row=4, column=2, sticky="nsew")
entrada5.config(yscrollcommand=scrolvert.set)# para que el escrol siga la posicion del texto

#boton
def codigoBoton():
    print("se enviaron correctamete los datos")
    
boton=Button(raiz, text="enviar", command=codigoBoton)
boton.pack()


raiz.mainloop()