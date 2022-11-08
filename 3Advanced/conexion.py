import mysql.connector # libreria para relizar las conexiones entre .py y sql

connection=mysql.connector.connect( # creamos la conexion
          host='localhost',
          port=3306,
          user='root',
          password='1234567',
          db='holaMysql'
   )

if connection.is_connected(): #funcion para saber si efectivamente nos conectamos
        print("conectado a la bd")

        info_server=connection.get_server_info() # funcio ver la version del servidor
        print(info_server)
else:
    ("no se a logrado conetar a la base de datos")

cursor = connection.cursor() # la funcion cursor nos permite interactuar con nuestras bases de datos

cursor.execute("SHOW DATABASES") # funcion para enviar comandos de SQL

for bd in cursor: # imprimimos la bd
    print(bd)

cursor.execute("select * from animales") 

for bd in cursor:# iprimimos la tabla de la bd
    print(bd)


connection.close()