#eliminar tabla completa 

import mysql.connector

conn=mysql.connector.connect(
         host="localhost",
         port=3306,
         user="root",
         password="1234567",
         db="pruebaa"
)

micursor=conn.cursor()

# eliminar tabla 
'''
sql="DROP TABLE customers"   

micursor.execute(sql)
'''
# para que el programa no vote error
sql2="DROP TABLE IF EXISTS customers"# si la tabla existe eliminela 

micursor.execute(sql2)