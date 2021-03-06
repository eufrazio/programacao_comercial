# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-08 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('sexo', models.SmallIntegerField(choices=[(1, 'Masculino'), (2, 'Feminino')])),
                ('data_nascimento', models.DateField()),
                ('estado_civil', models.SmallIntegerField(choices=[(1, 'Solteiro'), (2, 'Casado'), (3, 'Viuvo'), (4, 'Divorciado'), (5, 'Outro')])),
                ('profissao', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('medico_responsavel', models.CharField(max_length=100)),
                ('alergia', models.CharField(max_length=100)),
                ('uso_medicamento', models.CharField(max_length=100)),
            ],
        ),
    ]
