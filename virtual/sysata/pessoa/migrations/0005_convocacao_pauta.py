# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-03 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0004_convocacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='convocacao',
            name='pauta',
            field=models.TextField(default=''),
        ),
    ]