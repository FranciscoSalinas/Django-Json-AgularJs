# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-21 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_auto_20160721_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='apellido',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='materia',
            name='descripcion',
            field=models.TextField(default='descripcion', max_length=150),
        ),
    ]
