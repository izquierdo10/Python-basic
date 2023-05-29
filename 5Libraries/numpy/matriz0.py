
lista=[[1,2,3],[4,5,6]]
tupla=(1,2,3)
conjunto={1,2,3}
dicionario={"uno":1,"dos":2,"tres":3}

print(type(lista))
print(type(tupla))
print(type(conjunto))
print(type(dicionario),"\n")

import numpy

arreglo=numpy.array([[1,2,3],[4,5,6]])

print(type(arreglo))
print(arreglo)
print("la diminecion de la matriz es:",arreglo.ndim)
print(arreglo[1][0])

