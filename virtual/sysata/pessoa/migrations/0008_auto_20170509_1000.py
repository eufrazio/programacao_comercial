# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-09 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0007_convocacao_convocados'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convocacao',
            name='convocados',
            field=models.ManyToManyField(to='pessoa.Pessoa'),
        ),
    ]