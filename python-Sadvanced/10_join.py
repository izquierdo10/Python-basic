# union de columnas de las tablas que tenga la base de datos 
# los join o union solo tienen la funcion de consulta

import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234567",
    db="pruebaa"
)

micursor= conn.cursor()

# JOIN INNER:
#Esta cláusula(INNER) busca coincidencias entre 2 tablas, en función a una columna que tienen en común. De tal modo que sólo la intersección se mostrará en los resultados.
sql = "SELECT \
  personas.Nombre AS personas, \
  productos.Nombre AS productos \
  FROM personas \
  INNER JOIN productos ON personas.id = productos.id"

micursor.execute(sql)

datos = micursor.fetchall()

for x in datos:
  print(x) 
