#ejercicio de lista y conjuntos

'''
Colecciones - Ejercicio 2: 
Escriba un programa que tenga dos listas y que, a continuación, cree las siguientes listas (en las que no debe haber repeticiones):

- Lista de elementos que aparecen en las dos listas.
- Lista de elementos que aparecen en la primera lista, pero no en la segunda.
- Lista de elementos que aparecen en la segunda lista, pero no en la primera.
- Lista de elementos que aparecen en ambas listas.
'''

lista1 = [1,2,3,4,4,4,5,5,6,7,7,7,8,8,9,9,10,"andres","alejandra",2,"andres",0]
lista2 = ["azul",50,1,2,2,6,7,8,"azul","perro","gato",10,"gato","rojo",0,11,9,50,"1"]

# para mostrar las dos lista sin valores repetidos
listaU = lista1+lista2 #unimos las dos listas 

listaU= list(set(listaU)) #convertimos la lista en conjunto para depues imprimir ese conjunto en lista
print(listaU)

#-----------------------------------------------------------------------------------------------------------------

# o tambien  podemos hacerlo de esta manera para manejar todas las operaciones
# matematicas que tiene los conjuntos ((unión, intersección, complemento y diferencia).)
a= set(lista1)
b= set(lista2)

print("union de listas",(a|b))
print("elemnto que solo tiene la primera lista",(a-b))
print("elemnto que solo tiene la segunda lista",(b-a))
print("elemnto que aparecen en las dos listas",(a^b))


