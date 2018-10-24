from django.db import models
from django.utils import timezone
from .validators import run_validation

# Create your models here.

class Adoptante(models.Model):
	correo = models.EmailField()
	run = models.CharField(max_length=10, validators=[run_validation], primary_key=True)
	nombreCompleto = models.CharField(max_length=100)
	#fechaNacimiento = models.DateField()
	telefono = models.CharField(max_length=9)
	#region = models.CharField(max_length=100)
	#ciudad = models.CharField(max_length=100)
	#vivienda = models.CharField(max_length=100)
	def __str__(self):
		return self.correo

class Adoptado(models.Model):
	idPerro = models.AutoField(primary_key=True)
	fotografia = models.ImageField()
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=30)
	descripcion = models.TextField()
	estado = models.CharField(max_length=10)
	def __str__(self):
		return self.nombre
