# el try_except conocido en otros leguajes de programacion como el try_catch
# nos permite controlar errores y que el programa termine.


try:# muestreme el error con mi mensaje
  print (10/"a")
except:
  print("ERROR EN EL PROGRAMA") 


try: # muestreme el error con mi mensaje y el typo de error.
  print (10/0)
except Exception as E: # execption avarca todos los erros que reconoce python y a esta se le asigna una varilabe con "as" 
  print("ERROR EN EL PROGARMA DE TIPO: ",E) 

print("el progama cotinua------------>")
NUM=(int(input("ingresa culaquier numero :")))
print("numero",NUM,"guardado")

try:
  print (10/"w")
except Exception as E:
  print("ERROR EN EL PROGARMA DE TIPO: ",E) 
finally: # el finally hara lo que se le indique asi haya error o no.
    print("fin del programa")
