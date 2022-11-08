#  Pedir tres números y determinar cuál es el mayor

num1 =int(input("ingrese el primer numero:"))
num2 =int(input("ingrese el segundo numero:"))
num3 =int(input("ingrese el tercer numero:"))

'''
if,elif,else los condicionales se abren con: y se 
cierran finalizando la sangría o indentación como lo vemos de ejemplo con el print.
'''
if num1>num2 and num1>num3:                #se tiene que cumplir las dos condiciones
    print(f"el numero mayor es: {num1} ")
elif num2>num3:                            # si se cumple
    print(f"el numero mayor es: {num2} ")
else:                                      # si las demas no se cumplen
    print(f"el numero mayor es: {num3} ")

print("final de condicion") #Si las demás no se cumplen


