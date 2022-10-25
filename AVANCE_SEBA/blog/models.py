from django.db import models

# Create your models here.

class BlogsPost(models.Model):

    title = models.CharField (max_length = 150) # Título del Blog

    username = models.TextField(max_length=20, blank=True, null=True) # Prueba de insertación del nombre de un usuario

    body = models.TextField (max_length = 200) #Cuerpo del blog

    timestamp = models.DateTimeField () #Hora de creación del blog
