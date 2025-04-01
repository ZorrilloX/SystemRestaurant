from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    nit = models.IntegerField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre}, nit: {self.nit}"