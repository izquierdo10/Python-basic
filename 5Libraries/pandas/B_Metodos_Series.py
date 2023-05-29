import pandas as pd
#metodos 
colores= pd.Series(["Amarillo","Azul","Rojo","verde"])

print(colores.size)
print(colores.index)

#operaciones aritmeticas 
numeros = pd.Series([1,2,3,4])
print(numeros*2)