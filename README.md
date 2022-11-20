<p align="center">
  <img width="30%" height="50%" src="https://www.python.org/static/img/python-logo.png">
</p>


# *Python-levels* 🐍

[![Python](https://img.shields.io/badge/Python-3.9+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
---
##### *Basic* -------------------->*15 ejercicios*
- [x] si  
- [ ] no   

##### *Intermediate* ------------->*15 ejercicios*
- [x] si 
- [ ] no

##### *Advanced* ----------------->*15 ejercicios* 
[![](https://img.shields.io/badge/MySQL-8.0.31-aqua)](https://dev.mysql.com/downloads/mysql/) [![conexion mysql](https://img.shields.io/badge/mysql--connector--python-8.0.31-blue)](https://pypi.org/project/mysql-connector-python/#history) 
- [x] si             
- [ ] no

##### *Expert* ------------------->*15 ejercicios* 
[![dj](https://img.shields.io/badge/Django-4.1.3-green)](https://www.djangoproject.com/) [![sqlite3](https://img.shields.io/badge/DB%20Browser%20for%20SQLite-3.12.2-lightgrey)](https://sqlitebrowser.org/) 
- [x] si 
- [ ] no

### *Creación de proyecto*

creamos una carpeta y dentro de esta con el cmd escribimos el siguiente comando:

```` django-admin startproject <nombre del proyecto> ```` --> Creación de archivo 

```` python manage.py migrate ```` --> migracion de la BD por defecto sqlite3

```` python manage.py runserver ````--> conexion al servidor django
  
--------------------------------------------------------------------------
  
### *Creación de un proyecto con apps*

```` django-admin startproject <nombre del proyecto> ```` --> creacion de archivo 

```` python manage.py startapp <nombre de la app> ```` --> creacion de la aplicacion 


configuracion previa al comando check:
 
1) creacion de las tablas de la BD en archivo models.py
  
2) instalar la app en archivo settings.py linea 40...

```` python manage.py check <nombre de la app> ```` ---> para verificar que la app se integro correctamente al proyecto. 

```` python manage.py makemigrations ```` ---> migracion de la app

```` python manage.py sqlmigrate <nombre de la app> <numero de migracion> ```` --> pasar y crear las tablas realizadas en el archivo models.py a lenguaje sql.

```` python manage.py migrate ```` --> creacion de la BD con el contenido previamente realizado 

------------------------------------------------------------------------

*insertar, modificar, borrar y ver datos de la BD desde el shell*
````
python manage.py shell --> ingresar al shell

from <nombre de la app>.models import <nombre de la clase> ---> llamar models del proyecto

<variable>=<nombre de la clase>(atributo='valorX')   ---> insertar datos 
<variable>.save()  --> guardar y realizar los cambios en la BD 

<variable>.atributo='valorA' --> modifique el valor del atributo
<variable>.save()

<variable>=<nombre de clase>.objects.get(id=2) --> borrar un dato
<variable>.delete()

lista=<nombre clase>.objects.all() --> nos mostrara cuantos id tiene el objeto
lista --> lo llamamos 
lista.query.__str__() --> nos mostrara los atributos que tiene el objeto o clase
````

*consultas con criterios*
````
where: 
<clase>.objects.filter(atributo='valorX') muestreme todos los valores con valores iguales 
.en archivo models.py linea 19 se le agrego un plus a la consulta

> <:
<clase>.objects.filter(atributo__gte=100) muestreme los valores que sean mayor a 100   
<clase>.objects.filter(atributo__lte=100) muestreme los valores que sean mmenor a 100 

orden_by:
<clase>.objects.filter(atributo__lte=50).order_by('atributo') ascendente
<clase>.objects.filter(atributo__lte=50).order_by('-atributo') descendente
````
<p align="center">
  <img width="12%" height="20%" src="https://img.shields.io/badge/%40-izquierdo10-Black">
</p>
