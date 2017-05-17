# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-03 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_auto_20170502_1113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convocacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_convocacao', models.DateTimeField()),
                ('tema', models.CharField(max_length=100)),
                ('presidente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
        ),
    ]