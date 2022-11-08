# unino a la izquierda 
'''
A diferencia de un INNER JOIN, donde se busca una intersección respetada por ambas tablas, con LEFT JOIN damos prioridad a la tabla de la izquierda,
 y buscamos en la tabla derecha.

Si no existe ninguna coincidencia para alguna de las filas de la tabla de la izquierda, de igual forma todos los resultados de la primera tabla se muestran.
'''

import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234567",
    db="pruebaa"
)

micursor= conn.cursor()

sql = "SELECT \
  personas.Nombre AS personas, \
  productos.Nombre AS productos \
  FROM personas \
  LEFT JOIN productos ON personas.id = productos.id"

micursor.execute(sql)

datos = micursor.fetchall()

for x in datos:
  print(x) 