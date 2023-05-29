import numpy as np

arreglo = np.array([[[1,1,1],[2,2,2]],[[3,3,3],[4,4,4]]])
arreglo4 = np.array([[[[1,9],[2,4]],[[3,6],[4,8]],[[5,10],[6,12]],[[7,14],[8,16]]]])
# si la array es de 3 dimenciones cree tres bucles para imprimir los elementos 
# 2 dimenciones, 2 bucles etc...

for matriz in arreglo: # 3d
            for filas in matriz:
                for elementos in filas:
                    print(elementos,end=" ")
#-----------------------------------------------------
print()
for matriz in arreglo4: # 4d
        for filtro in matriz:
            for filas in filtro:
                for elementos in filas:
                    print(elementos,end=" ")
                    
