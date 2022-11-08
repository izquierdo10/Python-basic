#bulce para con funcion range()

#pograma que te muestra la tabla de multiplicar del numero ingresado

num=int(input("ingrese el numero a multiplicar: "))

print("desea inrgresar el rango de la multiplicacion o dejarlo por defecto")
decision=input("ingrese si(para cambirlo) \ningrese no (para dejarlo por defecto= multiplique hasta 10)\n")


#condicion
if decision=="si":
    rango=int(input("ingrese el rango que desea:"))
else:
    rango=11


print("tabla del:",num)


for i in range(rango):
    mult=num*i       #multiplicador
    print(num,"X",i,"=",mult)
