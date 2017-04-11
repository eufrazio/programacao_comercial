from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pessoa(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.IntegerField()
	telefone = models.IntegerField()
	email = models.CharField(max_length=100)
	departamento = models.SmallIntegerField(choices=[(1, 'VENDAS'), (2, 'ADMINISTRACAO'), (3, 'APOIO')])

	def __str__(self):
		return '{0} - {1} ({2}/{3})'.format(self.nome, self.email, self.telefone, self.departamento)