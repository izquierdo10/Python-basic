# llamar el numero de registro que desea

import mysql.connector

conn=mysql.connector.connect(
         host="localhost",
         port=3306,
         user="root",
         password="1234567",
         db="pruebaa"
)

micursor=conn.cursor()

sql="SELECT * FROM personas LIMIT 2"

micursor.execute(sql)

dato=micursor.fetchall()

for x in dato:
    print(x)

print("------------------------------------")
# si desea llamar el numero de registros, a partir de una x posicion se usa el "OFFSET"

sql2="SELECT * FROM personas LIMIT 2 OFFSET 3"

micursor.execute(sql2)

datos2=micursor.fetchall()

for x in datos2:
    print(x)



