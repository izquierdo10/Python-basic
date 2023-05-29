import pandas as pd 
# para poder mezclar dos dataf  ahi que tener un culumna clave en cada dataF
#en este ejemplo la columna clave es MARCA
dataF1 = pd.DataFrame({"MARCA":["Nissan","Ford","mercedes-benz"],
                        "MODELO":[2020,2023,2018],
                        "COLOR":["gris","Azul","Negro"]})

dataF2 = pd.DataFrame({"MARCA":["Nissan","Ford","mercedes-benz"],
                        "PROPIETARIO":["Maria","Andres","Juan"],
                        "EDAD":[28,24,30]})

mezcla= pd.merge(dataF1,dataF2)

print(mezcla)