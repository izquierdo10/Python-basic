# sin el if in 
letra=input("ingrese una letra:")


if letra =="a" or letra =="e" or letra =="i"or  letra =="o" or letra =="u":
     print("la letra ingresada ",letra," si es una vocal")
else:
    print("la letra ingresada no es una vocal")



#con el if in y el if not in
vocales =["a","e","i","o","u","A","E","I","O","U"]

letra2=input("ingrese otra letra:")

if letra2 in vocales: # condicional if con in. in= evalua en la secuncia de la list,set,dict y objeto si hay un valor que consida dentro.
     print("la letra ingresada ",letra2," si es una vocal")
else:
    print("la letra ingresada no es una vocal")

if letra2 not in vocales: # condicional if con not in.  not in= evalua en la secuncia de la list,set,dict y objeto si no hay un valor que consida dentro.
     print("la letra ingresada ",letra2," no esta en el grupo de vocales ")



