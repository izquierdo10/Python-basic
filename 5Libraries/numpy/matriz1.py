import numpy as np

#dimenciones

arreglo = np.array(1)
arreglo1= np.array([1,2])
arreglo2= np.array([[1,9],[2,4]])
arreglo3 = np.array([[[1,9],[2,4]],[[3,6],[4,8]]])
arreglo4 = np.array([[[[1,9],[2,4]],[[3,6],[4,8]],[[5,10],[6,12]],[[7,14],[8,16]]]])
arreglo5 = np.array([[[[[1]]]]])

print(arreglo.ndim,"dimenciones") 
print(arreglo1.ndim,"dimencion") 
print(arreglo2.ndim,"dimenciones") 
print(arreglo3.ndim,"dimenciones") 
print(arreglo4.ndim,"dimenciones")
print(arreglo5.ndim,"dimenciones","\n")
#lementos de posición final
print(arreglo)
print(arreglo1[1])
print(arreglo2[1][1])
print(arreglo3[1][1][1])
print(arreglo4[0][3][1][1])




