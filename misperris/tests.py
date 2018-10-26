from django.test import TestCase
from .models import Adoptante, Adoptado

# Create your tests here.
class AdoptanteTestCase( TestCase ):
    def testAdoptantesCrear( self ):

        #Arrange
        
        expected = 1
        result = 0

        #Act
        Adoptante.objects.create(correo="prueba@gmail.com", run=12345678-9, nombreCompleto="Prueba probadora asd asd", telefono=123456789, region="XIII Metropolitana de Santiago", vivienda="Casa con patio grande")
        result = len(Adoptante.objects.all())

        #Assert
        self.assertEqual(expected,result)

    

    def testAdoptantesEliminar( self ):

        #Arrange
        
        expected = 0
        result = 1

        #Act
        Adoptante.objects.all().delete()
        result = len(Adoptante.objects.all())

        #Assert
        self.assertEqual(expected,result)


    def testAdoptantesEliminarConParametros( self ):

        #Arrange
        
        expected = 0
        result = 1

        #Act
        Adoptante.objects.create(correo="prueba@gmail.com", run=12345678-9, nombreCompleto="Prueba probadora asd asd", telefono=123456789, region="XIII Metropolitana de Santiago", vivienda="Casa con patio grande")
        Adoptante.objects.filter(run=12345678-9).delete()
        result = len(Adoptante.objects.all())

        #Assert
        self.assertEqual(expected,result)



