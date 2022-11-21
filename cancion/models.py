from django.db import models

# Create your models here.
class Cancion(models.Model):
    id_cancion = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=100)
    duracion = models.CharField(max_length=30)
    letra = models.CharField(max_length=10000)