import pandas as pd
#https://www.youtube.com/watch?v=zDTs_BzQMJk&list=PLg9145ptuAig5cwvUCn9FNSUJyXBiFcVg&index=11
DataF = pd.read_csv('pandas\W_datosParaPanda.csv')

#agregar filas
nueva_fila = ['Camila','Saenz Contrera',24,345796844,'camilaSC@example.com']
DataF.loc[len(DataF)] = nueva_fila

#agregar columnas y datos 
DataF['Profecion'] = pd.Series(['Medico','Ingeniero','Abogado','Profesor','Arquitecto'])

# Guardar el DataFrame en un nuevo archivo CSV
DataF.to_csv('pandas/X_datosParaPandaModificado.csv', index=False)

print(DataF)
