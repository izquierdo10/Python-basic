import pandas as pd 

colores = pd.Series(["Amarillo","Azul","Rojo","Verde","Naranja"])

print(colores[0:1])
print(colores [1:])
print(colores[3:4])

numeros = pd.Series({"uno":1,"dos":2,"tres":3,"cuatro":4})

print(numeros["dos"])
print(numeros[["cuatro","uno"]])# Dos corchetes para llamar más de un elemento del diccionario
print(numeros[numeros>2]) #Recorriendo con una condición