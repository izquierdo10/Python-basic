import numpy as np
#arr 1d = 2**0= 1 elemento
#arr 2d = 2**1= 2 e
#arr 3d = 2**2= 4 e
#arr 4d = 2**3= 8 e
#arr 5d = 2**4= 16 e

arr = np.array([[[[[1,"a"],[2,"b"]]],[[[3,"c"],[4,"d"]]],[[[5,"e"],[6,"f"]]],[[[7,"g"],[8,"h"]]],[[[9,"i"],[10,"j"]]],[[[11,"k"],[12,"l"]]],[[[13,"m"],[14,"n"]]],[[[15,"o"],[16,"p"]]]]])

print("array de:",arr.ndim,"D")
print(arr[0][4][0][1][0])

#palabra
print(arr[0][0][0][0][1],end="")
print(arr[0][5][0][1][1],end="")
print(arr[0][3][0][0][1],end="")
print(arr[0][7][0][0][1],end="")