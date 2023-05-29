from numpy import random
#crear una array con el modulo random

enteros = random.randint(10 , size=(4,4))
print(enteros)

decimal = random.rand(2,2)
print(decimal)

# elegir de forma aleatoria, sorteo:
nombres=["Jhon","will","Marta","Jeny","luz","Tom","James","Noah","Sebastian","Sophia"]
ganador=random.choice(nombres)
print("El ganador es:"+ganador)



