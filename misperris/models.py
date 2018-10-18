from django.db import models
from django.utils import timezone

# Create your models here.

class Adoptante(models.Model):
	correo = models.CharField(max_length=200)
	run = models.CharField(max_length=10, primary_key=True)
	nombreCompleto = models.CharField(max_length=100)
	fechaNacimiento = models.DateField()
	telefono = models.IntegerField()
	region = models.CharField(max_length=100)
	ciudad = models.CharField(max_length=100)
	vivienda = models.CharField(max_length=100)

class Adoptado(models.Model):
	fotografia = models.TextField()
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=30)
	descripcion = models.TextField()
	estado = models.CharField(max_length=10)
