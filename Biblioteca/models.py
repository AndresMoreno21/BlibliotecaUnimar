from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.


CATEGORIA_CHOICES = (('Acción y aventuras', 'Acción y aventuras'),
              ('Ciencia', 'Ciencia'),
              ('Ficción', 'Ficción'),
              ('Cómics', 'Cómics'),
              ('Cuentos', 'Cuentos'),
              ('Erótica', 'Erótica'),
              ('Fantástica', 'Fantástica'),
              ('Humor', 'Humor'),
              ('Infantil', 'Infantil'),
              ('Misterio', 'Misterio'),
              ('Narrativa', 'Narrativa'),
              ('Terror', 'Terror'))

class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    categoria = models.CharField(max_length=200, choices= CATEGORIA_CHOICES)
    paginas = models.CharField(max_length=100)
    fragmento =  models.TextField(max_length=1000)

    def __str__(self):
        return self.titulo   

class Editorial(models.Model):
    nit = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono  = models.CharField(max_length=100)
    email  = models.CharField(max_length=100)
    libros = models.ManyToManyField(Libro)
    sitioweb = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to = 'media/')

    def __str__(self):
        return self.nombre


    






