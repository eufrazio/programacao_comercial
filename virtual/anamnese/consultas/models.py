from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Doenca(models.Model):
	doenca = models.CharField(max_length=100)


class Sintoma(models.Model):
	sintoma = models.CharField(max_length=100)

	def __str__(self):
  		return '{0}'.format(self.sintoma)

class Doenca_Sintoma(models.Model):
	 fk_doenca = models.ForeignKey(Doenca, on_delete=models.CASCADE)
	 fk_sintoma = models.ForeignKey(Sintoma, on_delete=models.CASCADE)

class Pergunta(models.Model):
	pergunta = models.CharField(max_length=200)

	def __str__(self):
  		return '{0}'.format(self.pergunta)
	
