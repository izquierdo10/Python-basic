# ordenar la consulta de forma ascendente o descendente 

import mysql.connector

conn=mysql.connector.connect(
         host="localhost",
         port=3306,
         user="root",
         password="1234567",
         db="pruebaa"
)

micursor=conn.cursor()

sql = "SELECT * FROM personas ORDER BY id"

micursor.execute(sql)

dato1 = micursor.fetchall()

for x in dato1:
  print(x)

print("---------------------")

sql2 = "SELECT * FROM personas ORDER BY id  DESC"

micursor.execute(sql2)

dato2 = micursor.fetchall()

for x in dato2:
  print(x)