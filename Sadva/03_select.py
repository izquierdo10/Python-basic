# selecciona una tabla y ver sus datos

import mysql.connector 

conn=mysql.connector.connect(
          host='localhost',
          port=3306,
          user='root',
          password='1234567',
          db="pruebaa"
)

micursor= conn.cursor()

micursor.execute("SELECT * FROM personas") # comando SQL SELECT = seleccionamos la tabla 

datos= micursor.fetchall() # primero guardamos los datos seleccionados y despues convertimos esos datos en tuplas con fetchall()

for x in datos:  # imprimimos los datos de la tabla selecionada 
    print(x)