#funcion que devuelva un valor

def suma( num, num2, num3): # funcion suma de tres valores
    resultado=num+num2+num3
    return resultado

print(suma(5,10,15))

print("")
#------------------------------------------------------------
def calculadora(num, num2): #funcion calculadora

    suma=("suma:",num+num2)
   
    resta=("resta:",num-num2)
   
    multi=("multiplicacion:",num*num2)
   
    div=("divicion:",num/num2)
    
    return suma,resta,multi,div

print(calculadora(5,5)) # ingrese dos valores y muestreme el resultado de la funcion calculadora



