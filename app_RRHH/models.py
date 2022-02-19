from pyexpat import model
from django.db import models

# Create your models here.
class PuestoLaboral(models.Model):
    PROCESO_CHOICES = (
        ('P','Produccion'),
        ('C','Calidad'),
        ('R','RRHH'),
        ('A','Administracion'),
        ('E','Expedicion'),
        ('T','Tecnica'),
    )
    area_laboral = models.CharField(max_length=1, choices=PROCESO_CHOICES)
    puesto_laboral = models.CharField(max_length=30)
    descrpcion = models.TextField()

    def __str__(self):
        return f'{self.area_laboral} - Puesto laboral: {self.puesto_laboral}'

class Empleado(models.Model):
    SEXO_CHOICES = (
        ('M','Masculino'),
        ('F','Femenino'),
    )
    nombre = models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    dni = models.CharField(max_length=8, verbose_name='DNI')
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fec_nac = models.DateField(verbose_name='fecha nacimiento')
    puesto = models.OneToOneField(PuestoLaboral, on_delete=models.CASCADE)
    fec_ing = models.DateField(verbose_name='fecha ingreso')
    activo = models.BooleanField(default=False, verbose_name='Empleado activo?')
    
    def __str__(self):
        if self.activo:
            return f'Empleado {self.nombre} {self.apellido} - Area: {self.puesto.puesto_laboral}'
        else:
            return f'Persona {self.nombre} {self.apellido} - No Activo(a)'