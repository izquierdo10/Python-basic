#crear base de datos 

import mysql.connector # importamos el conector 

conn=mysql.connector.connect( # creamos la conexion
          host='localhost',
          port=3306,
          user='root',
          password='1234567',
          
   )

micursor= conn.cursor() # creamos el cursor, quien nos permitira trabajar con la BD

micursor.execute("CREATE DATABASE pruebaa") # la funcion .execute nos permite enviar comandos SQL