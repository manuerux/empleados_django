from django.db import models
from ..departamento.models import Departamento

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'

    def __str__(self):
        return str(self.id) + "-" + self.habilidad

class Empleado(models.Model):
    """modelo para tabla empleado"""
    TIPOS_JOB = (
        ('0', 'Contador'),
        ('1', 'Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombre Completo', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=50, choices=TIPOS_JOB)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    Habilidades = models.ManyToManyField(Habilidades)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
