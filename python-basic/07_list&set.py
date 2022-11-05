# ejercicio de lista y conjuntos
# eliminar valores repetidos de una lista y al final muestre una lista sin estas repeticiones.

lista =[1,1,1,2,2,43,3,43,"uno","dos",6,7,4,5,"uno","tres"]

print (lista)

lista2 = list(set(lista))



print (lista2)
print("la lista con repeticiones tiene un total de: ",len(lista))
print("la lista si repeticiones tien un total de: ",len(lista2))
total=len(lista)-len(lista2)
print("numero de valores repetidos:",total)