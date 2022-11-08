#creacion de una segunda tabla para la practiva de los JOINS

import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="1234567",
    db="pruebaa"
)

micursor= conn.cursor()


sql="CREATE TABLE productos (id INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), precio INT(255))"

micursor.execute(sql)
#---------------------------------------------------------------------------

sql2="INSERT INTO productos (Nombre,precio) VALUES (%s,%s)"
val=[
('papas',1000),
('jugo',1200),
('dulces',500),
('agua',1000),
('fruta',800),
('chocolate',800),
('mani',500),
('tabaco',500)
]

micursor.executemany(sql2,val) # funcion executemany() para enviar mas de un dato

conn.commit()

print(micursor.rowcount, "valores insertados.") # confirmamos que se insertaron los valores.