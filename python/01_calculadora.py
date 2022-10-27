#Calculadora

nombre= input("ingresa tu nombre: ") #Escáner o entrada de datos con un mensaje en él, sin necesidad de un print
print("hola!! ",nombre)


print("ingrese el primer numero:")
Pnumero= int(input()) # Escáner o entrada de datos declarando el tipo int

print("ingrese el segundo numero:")
Snumero=int(input())

# Operadores aritméticos 
suma = Pnumero + Snumero
res = Pnumero - Snumero
div = Pnumero / Snumero
mult = Pnumero * Snumero
expo = Pnumero ** Snumero
por = Pnumero %  Snumero 

print("\n suma:",suma,"\n resta:",res,"\n divicion:",div,"\n multiplicacion:",mult,"\n exponenciacion:",expo,"\n porcentaje:",por,"%")

