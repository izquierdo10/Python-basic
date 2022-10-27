#arrays o matriz
# sacar corchetes [] Alt Gr + tecla a la derecha de p


print("\n lista1")
#posicion real:
#       0,1,2,3,4,   5  ,6,7,    8   ,9,  10   ,11,12, 13   ,   14   ,   15   ,16.
list = [1,2,3,4,5,"hola",6,7,"buenas",8,"noches",9,10,"dias","tardes","buenos",0]



print(list)       # imprimir lista
print(len(list))  # imprimir numero de indices de la lista
print(list[4:14]) # imprimir un inidce hasta el otro indice inidicado -->
print(list[-10:]) # imprimir de forma contraria o negativa <--
print(list.count("hola")) # imprime cuantas veces x varible se repite en la array


print("\n lista2")

list2 = [4,9,6,3,5,8,7,-5,-1,-2,-6,-10,0]
'''
tupla = (4,9,6,3,5,8,7,-5,-1,-2,-6,-10,0) la tupla se utliza si queremos que esta no se pueda modificar.
en tanto a lo demas, se usa de la misma forma que la list.
'''

print(list2) # imprime lista
list2.sort() # funcion imprimir por orden ascendente de menor a mayor 
print(list2) # imprime lista ordenada
list2.sort(reverse=True) # funcion imprimir por orden descendente de mayor a menor
print(list2)

print("\n agrega un nuevo valor a la lista 1:")
valor=input()    #escaner
list.append(valor)  # funcion para agregar valor a la lista

print(list)

print(list+list2) # union de listas