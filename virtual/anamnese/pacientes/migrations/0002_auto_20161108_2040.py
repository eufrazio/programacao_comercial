# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-08 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='data_nascimento',
            field=models.DateTimeField(),
        ),
    ]
