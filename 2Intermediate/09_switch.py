# simular un switch en python con:
# creacion de funcion, diccionario y funcion get()

def switch(num): 
    meses={
        1:"enero",
        2:"febrero",
        3:"marzo",
        4:"abril",
        5:"mayo",
        6:"junio",
        7:"julio",
        8:"agosto",
        9:"septiembre",
        10:"octubre",
        11:"nomviembre",
        12:"diciembre"
    }
    return meses.get(num,"mes no valido")

num=int(input("ingresa el numero del mes:"))
print(switch(num))