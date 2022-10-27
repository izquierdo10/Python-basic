# diccionario 
# en los diccionarios siempre tiene que ir la clave y despues el valor (clave:valor)

colores ={"amarillo":"yellow","azul":"blue","rojo":"red"}

print(colores)
print(colores.values()) # funcion ver los valores del diccionario
print(colores["azul"]) #imprimimos el valor de azul
print(len(colores)) # cuantos colores ahi en el diccionario 

numeros ={1:"one",2:"two",3:"three"}

print(numeros)
print(numeros.keys()) #funcion ver claves del diccionario
print(numeros[2]) # imprimimos el valor de 2

print("agrega un nuevo numero al diccionario: ")

leaC =int(input())
leaV =input()

numeros[leaC] = leaV #agregamos la clave:valor 

print(numeros)

''''''''''''''''''''''''
traductor = colores|{"1":"one","2":"two","3":"three"} # unificamos cambiando las claves a tipo str

print(traductor)
print("que color o numero quires traducir al ingles: ")

leaX =input() #leemos por teclado
print(traductor[leaX])













