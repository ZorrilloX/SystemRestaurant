# Generated by Django 5.1.7 on 2025-04-01 01:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_plato_alter_cliente_nit_alter_mesero_telefono'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('cliente_nit', models.CharField(blank=True, max_length=20, null=True)),
                ('estado', models.CharField(choices=[('abierta', 'Abierta'), ('cerrada', 'Cerrada')], default='abierta', max_length=10)),
                ('fecha_hora', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.cliente')),
                ('mesa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.mesa')),
                ('meseros', models.ManyToManyField(to='restaurant.mesero')),
                ('platos', models.ManyToManyField(to='restaurant.plato')),
            ],
        ),
    ]
