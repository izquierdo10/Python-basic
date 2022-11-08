# versiones de python desde la version 3.10 en incremeton permiten el uso de match
# lo cual es el switch que concemos en otros lenguajes.

Maquina_expendedora=(int(input("que producto quieres:")))


match Maquina_expendedora: # creamos el match
    case 1 : print("papas de pollo")
    case 2 : print("galletas ")
    case 3 : print("chocolatina")
    case 4 : print("jugo")
    case 5 : print("agua")
    case __: print("obcion no valida") # case por si se introduce un valor que no esta en el menu.

    



