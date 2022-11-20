from django.db import models

# Create your models here.

#la clase models nos permite manejar la BD (crear Tablas ,eliminar, crear campos, modificar etc...)
#como vemos las class tiene una relacion orientada a objeto

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    celular=models.CharField(max_length=10)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):# para poder ver mejor la consulta desde el shell
        return 'el nombre es %s la seccion es %s y el precio es %s' %(self.nombre,self.seccion,self.precio)

class Pedidos(models.Model):
     N_Pedido=models.IntegerField()
     Fecha=models.DateField()
     Entregado=models.BooleanField()
    
     def __str__(self):
        return 'el N de pedido %s la fecha fue  %s y la entrega %s' %(self.N_Pedido,self.Fecha,self.Entregado)


