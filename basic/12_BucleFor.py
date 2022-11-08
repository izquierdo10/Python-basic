#ciclo para 

# el ciclo para o bucle_for de ptyhon es muy diferente al que conocemos en otros lenguajes
# ya que este se utiliza para recorrer las (list,set,dict y cadenas srt) mas no es posible
# darle un numero determinado de repeticiones con un varible X sino que  este hara el recorido 
# segun el numero de indices o elementos que tenga las (list,set,dict y cadenas srt).

print("for de lista ////////////////////")
lista =[1,2,3,4,5,"a","z"]
for i in lista:
    print(i)


print("for de conjunto ////////////////////")
conjunto ={6,7,8,9,10,"a","b","c"}
for i in conjunto:
    print(i)
   

print("for de diccionario ////////////////////")
diccionario={"andres":23,"miguel":24,"sebastian":24,"camilo":21}
for clave,valor in diccionario.items():
    print(clave,valor)


print("for de nombre ////////////////////")
nombre ="Andres" #cadena srt
for i in nombre:
    print(".",i,".")
#or
for i in nombre:
    print(i,end=".") # quitamos el salto de linea con end=""