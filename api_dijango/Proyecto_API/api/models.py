from django.db import models

# Create your models here.
class Persona(models.Model):
    tipodocumento = models.CharField(max_length=50)
    documento = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    hobbie = models.CharField(max_length=50)