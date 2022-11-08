# elimiar datos de una tabla

import mysql.connector

conn=mysql.connector.connect(
         host="localhost",
         port=3306,
         user="root",
         password="1234567",
         db="pruebaa"
)

micursor=conn.cursor()

micursor.execute("DELETE FROM personas WHERE Nombre = 'johnn'")

conn.commit()

print(micursor.rowcount, "registro(s) eliminados")