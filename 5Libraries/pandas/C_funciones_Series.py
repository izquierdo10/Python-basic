import pandas as pd 

numeros = pd.Series([1,2,3,4,5,15,6,7,8,9])

#funciones basicas
print(numeros.max())
print(numeros.min())
print(numeros.std())
print(numeros.describe(),"\n")

materias =pd.Series({"matematicas":80,"economia":60,"programacion":100,
"fiscia":50})

#funciones avanzadas
print(materias.sort_values())#Imprima de forma ascendente
print(materias.sort_index(ascending=False))#Imprima de forma Descendente o ascendente


