from __future__ import unicode_literals

from django.db import models
from datetime import datetime 

# Create your models here.

class Paciente(models.Model):
  nome = models.CharField(max_length=100)
  idade = models.IntegerField()
  sexo = models.SmallIntegerField(choices=[(1, 'Masculino'), (2, 'Feminino')])
  data_nascimento = models.DateField()
  estado_civil = models.SmallIntegerField(choices=[(1, 'Solteiro'), (2, 'Casado'), (3, 'Viuvo'), (4, 'Divorciado'), (5, 'Outro')])
  profissao = models.CharField(max_length=100)
  endereco = models.CharField(max_length=100)
  medico_responsavel = models.CharField(max_length=100)
  alergia = models.CharField(max_length=100)
  uso_medicamento = models.CharField(max_length=100)


  def __str__(self):
    return '{0} - {1} ({2}/{3})'.format(self.nome, self.data_nascimento, self.medico_responsavel, self.alergia)

