from django.db import models

class Mesero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
