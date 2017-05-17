# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-15 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Convocacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(max_length=100)),
                ('data_convocacao', models.DateTimeField()),
                ('pauta', models.TextField(default='')),
            ],
            options={
                'verbose_name_plural': 'Convocacoes',
            },
        ),
        migrations.CreateModel(
            name='Membro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participacao', models.SmallIntegerField(choices=[(1, 'PRESIDENTE'), (2, 'SECRETARIO'), (3, 'PARTICIPANTE')])),
                ('data_membro', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.BigIntegerField()),
                ('telefone', models.BigIntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('departamento', models.SmallIntegerField(choices=[(1, 'VENDAS'), (2, 'ADMINISTRACAO'), (3, 'APOIO')])),
            ],
        ),
        migrations.AddField(
            model_name='membro',
            name='nome_pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa'),
        ),
        migrations.AddField(
            model_name='membro',
            name='tema_convocacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Convocacao'),
        ),
        migrations.AddField(
            model_name='convocacao',
            name='convocado',
            field=models.ManyToManyField(through='pessoa.Membro', to='pessoa.Pessoa'),
        ),
    ]
