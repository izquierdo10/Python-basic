#creacion de clase con metodo __str__


class campeones:

    def __init__(self,nombre="nombre",rol="rol",posicion="posicion"):
        self.nombre = nombre
        self.rol = rol
        self.posicion = posicion

    def __str__(self): # este metodo nos permite hacer un print afuera de la clase sin tener que llamar cada atributo
        return(f"{self.nombre} {self.rol} {self.posicion}")


variable=campeones("yasuo","luchador","mid") # llenamos el objeto
print(variable) # imprimimos todos los atributos del objeto

objeto=campeones() # objeto por defecto
print(objeto) 