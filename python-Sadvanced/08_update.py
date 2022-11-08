# actualizar registros existentes de una tabla 

import mysql.connector

conn=mysql.connector.connect(
         host="localhost",
         port=3306,
         user="root",
         password="1234567",
         db="pruebaa"
)

micursor=conn.cursor()

sql=" UPDATE personas SET Nombre = %s WHERE Nombre = %s " # va tomar el valor X y lo va a cambiar por el valor existente
val=("andres","johnnnn") # val=("valor x","valor existente")

micursor.execute(sql,val)

conn.commit()

print(micursor.rowcount, "registro(s) actualizado")