#ciclo mientras

#realizar un programa que me de la raiz cuadrada de un numero y si ingreso un numero
#negativo volver a pedir hasta que este se un numero positivo.

'''
 OBSERVACIÓN La raíz cuadrada de un número positivo siempre tiene dos valores, uno positivo y uno negativo, pues
  al elevar al cuadrado el signo siempre es positivo. El único número que tiene una sola raíz cuadrada es el cero.
Por el mismo motivo, NO EXITEN RAICES CUADRADAS DE UN NUMERO NEGATIVO.
'''
import math  # libreria para sacar la raiz Cuadrad 

leaNum=(int(input("ingrese un numero: "))) #imprime y guarda por teclado un tipo entero

while leaNum<0: # ciclo
    print("error el numero ingresado debe ser positivo")
    leaNum=(int(input("ingrese un numero: ")))


print("la raiz cuadrada de ",leaNum," es:",math.sqrt(leaNum)) #imprime la raiz con la funcion math.sqrt




