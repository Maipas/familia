from django.db import models

# Create your models here.
class Family(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    nacimiento= models.IntegerField()
    edad = models.IntegerField()
    estado = models.CharField(max_length=30)
    parentesco = models.CharField(max_length=30)
    active = models.BooleanField(default=True)
