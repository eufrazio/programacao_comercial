# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-09 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_auto_20161108_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='data_nascimento',
            field=models.DateField(),
        ),
    ]
