from django.db import models

from django.core.exceptions import ValidationError


class Orden(models.Model):
    ESTADO_CHOICES = [
        ('abierta', 'Abierta'),
        ('cerrada', 'Cerrada'),
    ]

    # Múltiples meseros y platos
    meseros = models.ManyToManyField('Mesero')
    platos = models.ManyToManyField('Plato')

    # Cada orden tiene una mesa obligatoria
    mesa = models.ForeignKey('Mesa', on_delete=models.CASCADE)

    # Cliente: se asigna al pagar. Se permite inicialmente null.
    cliente = models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True, blank=True)

    # Datos adicionales que se capturan al pagar
    cliente_nombre = models.CharField(max_length=100, blank=True, null=True)
    cliente_nit = models.CharField(max_length=20, blank=True, null=True)

    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='abierta')
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Evita que una mesa tenga más de una orden abierta al mismo tiempo
        if self.estado == 'abierta':
            qs = Orden.objects.filter(mesa=self.mesa, estado='abierta')
            if self.pk:
                qs = qs.exclude(pk=self.pk)
            if qs.exists():
                raise ValidationError("La mesa ya tiene una orden abierta.")

    def __str__(self):
        return f"Orden #{self.id} - Mesa {self.mesa.numero} - {self.estado}"
