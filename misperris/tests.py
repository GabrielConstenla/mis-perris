from django.test import TestCase
from .models import Adoptante, Adoptado

# Create your tests here.

class AdoptanteTestCase( TestCase ):
    def Test_Adoptantes( self ):

        #Arrange
        size = len(Adoptante.objects)
        expected = 1
        result = 0

        #Act
        Adoptante.objects.create(correo="prueba@prueba.com", run=1234567890, nombreCompleto="Prueba probadora asd asd ", fechaNacimiento="1990-12-12", telefono=123456789, region="Metropolitana de Santiago", ciudad="Maipú", vivienda="Casa con patio grande")
        result = len(Adoptante.objects)

        #Assert
        self.assertEqual(expected, result)

    def Test_Adoptados(self): #o setUp()
        #Arrange
        size = len(Adoptado.objects)
        expected = 1
        result = 0

        #Act
        Adoptado.objects.create(idPerro= 1, fotografia= "asd", nombre= "k chupin", raza= "kachupinio", descripcion="Perrito k chupin", estado="adoptado")
        result = len(Adoptado.objects)

        #Assert

        self.assertEqual(expected, result)
