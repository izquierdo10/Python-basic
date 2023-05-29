import numpy as np

arr = np.array([9,2,4,5,6,1,8,7,3,0])

x= np.where(arr == 8)# nos permite enctrar la posicion de un elemento
                        #GRAN UTILIDAD
print(x)

arr2 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

z = np.where(arr2 == 8)
print(z)

arr3 = np.array([[[[1],[2]],[[3],[4]],[[5],[6]],[[7],[8]]]])

y= np.where(arr3 == 8)
print(y)