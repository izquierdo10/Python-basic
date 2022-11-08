# donde esta x registro o dato 

import mysql.connector

conn=mysql.connector.connect(
         host="localhost",
         port=3306,
         user="root",
         password="1234567",
         db="pruebaa"
)

micursor=conn.cursor()

micursor.execute("SELECT * FROM personas WHERE id = 2 ")

dato= micursor.fetchall()

for x in dato:
    print(x)