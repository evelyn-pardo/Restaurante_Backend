from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

from restaurante import settings

class Mesa(models.Model):
    capacidad = models.IntegerField(default=2)  # Capacidad de la mesa, valor por defecto 2

class Menu(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    foto = models.ImageField("foto", upload_to='menu_fotos/', null=True, blank=True) 
    descripcion = models.CharField(max_length=255) 
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    def image_url(self):
        if self.foto:
            return f'{settings.MEDIA_URL}{self.foto}'
        return ''

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=10)
    num_comensales = models.PositiveIntegerField()
    celebracion = models.CharField(max_length=100)
    fecha = models.DateField()  # Guardar la fecha
    hora = models.TimeField()    # Guardar la hora
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)  # Relación con la mesa

    def __str__(self):
        return f"Reserva de {self.nombre} {self.apellido} para el {self.fecha} a las {self.hora}"

