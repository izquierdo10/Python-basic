# insertar datos en la tabla

import mysql.connector

conn=mysql.connector.connect( # creamos la conexion
          host='localhost',
          port=3306,
          user='root',
          password='1234567',
          db="pruebaa"
   )

micursor= conn.cursor()

sql = "INSERT INTO personas (Nombre, CC) VALUES (%s, %s)" #creamos variable con comandos SQL 
val = ("john", 156932036)  # creamos variable que guardara los datos Nombre y CC

micursor.execute(sql, val) # enviamos las dos variables a la BD

conn.commit() # la funcion .commit() le dira a la BD que tiene que guarda los datos insertados

print(micursor.rowcount, "record inserted.") # .rowcount Nos dirá cuantos registros exitosos se hicieron