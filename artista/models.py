from django.db import models
from cancion.models import Cancion

# Create your models here.

class Artista(models.Model):
    id_artista = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    sitio_web = models.CharField(max_length=50)

class Escriben(models.Model):
    id_escriben = models.CharField(max_length=10, primary_key=True)
    fk_cancion = models.ForeignKey(Cancion, null=True, blank=True, on_delete=models.CASCADE)
    fk_artista = models.ForeignKey(Artista, null=True, blank=True, on_delete=models.CASCADE)


