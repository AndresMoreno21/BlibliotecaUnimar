from django.db import models

# Create your models here.

class Editorial(models.Model):
    nit = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono  = models.CharField(max_length=100)
    email  = models.CharField(max_length=100)
    sitioweb = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to = 'Biblioteca/BibliotecaUnimar/templates/editorialMedia/')

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editorial = models.ForeignKey(Editorial, on_delete= models.CASCADE)
    paginas = models.CharField(max_length=100)
    fragmento =  models.TextField(max_length=200)
    






