# clases que heredan atributos y metodos de otra.

class cochefabrica: # clase madre: es la base y la que podemos ver tiene el constructor 
     def __init__(self,marca="marca",modelo="modelo",color="color"): #constructor 
         self.marca = marca 
         self.modelo = modelo
         self.color = color


     def __str__(self):
        return (f"{self.marca} {self.modelo} {self.color} ") #atributos de clase madre, esta no puede tomar los atributos de la clase hija 

class vendido(cochefabrica): # clase hija: puede heredar lo que tiene la clase madre (construtor y atributos)
     placa ="dfg-789"
     dueño ="alex"
       
     def __str__(self):
        return (f"{self.placa} {self.dueño} {self.marca} {self.modelo} {self.color} ") #atributos de clase hija , esta si puede tomar los atributos de la clase madre 

variable=cochefabrica() # llamamos la clase madre 
print(variable)

variable2=vendido()#llamamos la clase hija 
print(variable2)
variable2=vendido("nisaa","2000","azul") 
print(variable2)








