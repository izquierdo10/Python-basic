import pandas as pd

dataF = pd.read_csv("pandas\W_datosParaPanda.csv")

print(dataF['Nombres']=="Renata")# sin filtro
#-----------------------------------------------
filtro_nombres= dataF['Nombres']=="Renata" # creamos el filtro con la informacion que necesitamos
dataF_filtro=dataF[filtro_nombres] # creamos el dataframe apartir del filtro

print(dataF_filtro)

# conocido el concepto de forma mas resumida seria:
mostrar = dataF[(dataF['Nombres']=='Renata') & (dataF['Edad']<50)]

print(mostrar)

