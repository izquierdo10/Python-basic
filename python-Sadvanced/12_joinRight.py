# unino a la derecha
'''
En el caso de RIGHT JOIN la situación es muy similar, pero aquí se da prioridad a la tabla de la derecha.
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
  RIGHT JOIN productos ON personas.id = productos.id"

micursor.execute(sql)

datos = micursor.fetchall()

for x in datos:
  print(x) 