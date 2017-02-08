from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Imagen(models.Model):
    url = models.CharField(max_length=2000)
    idUsuario = models.CharField(max_length=20, primary_key=True, default='usuario')
    correo = models.CharField(max_length=150, default='correo@dominio.com')
    nombre = models.CharField(max_length=150, default='nombre')
    paisDeOrigen = models.CharField(max_length=50, default='Colombia')
    ciudad = models.CharField(max_length=50, default='Bogota')
    interesPorLaReserva = models.CharField(max_length=500, default='interes')
    foto = models.ImageField(upload_to='pic_folder/', default='pic_folder/default.jpg')

