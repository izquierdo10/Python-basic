#crear tabla en BD

import mysql.connector

conn=mysql.connector.connect( # creamos la conexion 
          host='localhost',
          port=3306,
          user='root',
          password='1234567',
          db="pruebaa"     # añadimos el nombre de la BD creada
   )

micursor= conn.cursor()


micursor.execute("CREATE TABLE personas (id INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), CC INT(255))")# comando SQL 