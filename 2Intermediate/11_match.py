# maquina expendedora que resive dinero, tiene dos formas de pedir los productos (letra o numero) y
# da el cambio segun lo que se pidio.


dinero=(int(input("ingresa dinero:")))


Maquina_expendedora=((input("elige el producto:")))

match Maquina_expendedora : # creamos el match
    case "1" | "a": print("papas de pollo $1200")
    case "2" | "b": print("galletas $1200 ")
    case "3" | "c": print("chocolatina $1200")
    case "4" | "d": print("jugo $1400")
    case "5" | "e": print("agua $1400")
    case "6" | "f": print("dulce $800")
    case "7" | "g": print("mentas $800")
    case "8" | "h": print("mani $1000")
    case "9" | "i": print("cheetos $1000")
    case "10"| "j": print("chicle $800")
    case __: print("obcion no valida") # case por si se introduce un valor que no esta en el menu.


precio1=800
precio2=1000
precio3=1200
precio4=1400

p3=["1","a","2","b","3","c"]
p1=["6","f","7","g","10","j"]
p2=[ "8","h","9","i"]
p4=["4","d","5","e"]

if Maquina_expendedora in p3:
     cambio = dinero-precio3
     print("su cambio $",cambio )

elif Maquina_expendedora in p1:
    cambio = dinero-precio1
    print("su cambio $",cambio )

elif Maquina_expendedora in p2:
    cambio = dinero-precio2
    print("su cambio $",cambio )

elif Maquina_expendedora in p4:
     cambio = dinero-precio4
     print("su cambio $",cambio )

