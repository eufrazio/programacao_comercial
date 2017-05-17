from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Pessoa(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.BigIntegerField()
	telefone = models.BigIntegerField()
	email = models.EmailField(max_length=100)
	departamento = models.SmallIntegerField(choices=[(1, 'VENDAS'), (2, 'ADMINISTRACAO'), (3, 'APOIO')])

	def __str__(self):
		return '{0} - {1} - {2} - {3})'.format(self.nome, self.email, self.telefone, self.departamento)

class Membro(models.Model):
	nome_pessoa = models.ForeignKey("Pessoa")
	participacao = models.SmallIntegerField(choices=[(1, 'PRESIDENTE'), (2, 'SECRETARIO'), (3, 'PARTICIPANTE')])
	tema_convocacao = models.ForeignKey("Convocacao")
	data_membro = models.DateTimeField(auto_now=False, auto_now_add=False)

	class Meta:
		unique_together = (("nome_pessoa", "tema_convocacao"),)

	def __str__(self):
		return '{0} - {1} - {2}'.format(self.nome_pessoa, self.participacao, self.tema_convocacao)

class Convocacao(models.Model):
	tema = models.CharField(max_length=100, unique=True)
	data_convocacao = models.DateTimeField(auto_now=False, auto_now_add=False)
	pauta = models.TextField(default='')
	convocados = models.ManyToManyField("Pessoa", through='Membro')

	class Meta:
		verbose_name_plural = "Convocacoes"

	def __str__(self):
		return '{0} - {1}'.format(self.tema, self.data_convocacao)





'''
class Pessoa(models.Model):
	nome = models.CharField(max_length=100)
	cpf = models.BigIntegerField()
	telefone = models.BigIntegerField()
	email = models.EmailField(max_length=100)
	departamento = models.SmallIntegerField(choices=[(1, 'VENDAS'), (2, 'ADMINISTRACAO'), (3, 'APOIO')])

	def __str__(self):
		return '{0} - {1} ({2}/{3})'.format(self.nome, self.email, self.telefone, self.departamento)

class Convocacao(models.Model):
	presidente = models.ForeignKey("Pessoa", related_name='pessoa_presidente')
	secretario = models.ForeignKey("Pessoa", related_name='pessoa_secretario', default='')
	data_convocacao = models.DateTimeField(auto_now=False, auto_now_add=False)
	tema = models.CharField(max_length=100)
	pauta = models.TextField(default='')
	convocados = models.ManyToManyField("Pessoa")

	class Meta:
		verbose_name_plural = "Convocacoes"

	def __str__(self):
		return '{0} - {1} - {2}'.format(self.presidente, self.data_convocacao, self.tema)
'''