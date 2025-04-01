from django.db import models

class Plato(models.Model):
    nombre = models.CharField(max_length=40, unique=True)
    descripcion = models.CharField(max_length=120)

    def __str__(self):
        return f"Plato {self.nombre}"
