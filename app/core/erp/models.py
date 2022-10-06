from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

class Tipo(models.Model):

    nombre = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['id']


class Categoria(models.Model):

    nombre = models.CharField(max_length=150, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class Empleado(models.Model):

#trabajar relacion
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
#tabla detalle
    categ=models.ManyToManyField(Categoria)

#columnas
    nombre = models.CharField(max_length=150, verbose_name='Nombres')
    dpi = models.CharField(max_length=10, unique=True, verbose_name='DPI')
    fecha_registro = models.DateField(default=datetime.now, verbose_name='Fecha_de_registro')
    fecha_creacion = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)
    año = models.PositiveIntegerField(default=0)
    salario = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    estado = models.BooleanField(default=True)
    genero = models.CharField(max_length=50)

    # gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['id']
