# conjuntos matemáticos 
# la diferencia de los conjuntos a las listas es que solo puede guardar datos únicos y a su vez
# se puede hacer operaciones matemáticas de conjuntos (unión, intersección, complemento y diferencia).
# set() función para conjuntos, si queremos convertir una lista, diccionario a conjunto

a ={1,2,3}
b ={3,4,5}

c={1,2,3,4,5,6,7,8,9,10}

print(a,b)

print(a==b) # diferencia
print(a|b) # union
print(a&b) # interseccion

print(a-b) # diferencia a
print(b-a) # diferencia de b
print(a^b) # diferencia simetrica a y b

print("agrega un elemento al conunto a:")
lea = int(input()) #scanner

a.add(lea) # funcion agregar en conjuntos
print(a)

print(a.issubset(c)) # si a es un subconjunto de c
print(c.issuperset(a|b)) # si c es un superconunto de a y b = complemento






