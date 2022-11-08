# creacion de clases
#las clases son una especie de funcion pero orientada a objetos
# POO = programacion orientada a objetos 
# un objeto tiene atributos

class Coche:   #creacion

    def __init__(self,marca='generico',modelo='0000',color='blanco'): # constructor def __init__(self)
        self.marca = marca                    
        self.modelo= modelo  # se crea la marca del constructor self | y luego se crea la marca del objeto
        self.color= color  

'''
ejemplo:
constructor:                           |objeto:
def __init__(self,marca,modelo,color): |class Coche:
 self.marca                            | marca
 self.modelo                           | modelo
 self.color                            | color
'''    

andres = Coche("nissan","2022","gris")  # llenamos el objeto
print(andres.marca,andres.modelo,andres.color) # imprimimos el objeto 

objeto=Coche() # objeto por defecto
print(objeto.marca,objeto.modelo,objeto.color)



