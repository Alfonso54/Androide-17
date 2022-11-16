from django.db import models

# Create your models here.

class Auto(models.Model):

    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    patente = models.CharField(max_length=100, blank=True)
    fecha = models.DateTimeField(auto_now=True)