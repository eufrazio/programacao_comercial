from django.test import TestCase
from django.core.urlresolvers import reverse
from medicos.models import *
from medicos.forms import *

# Create your tests here.

class TestViewMedicosList(TestCase):
  '''
  Classe de testes para a view MedicosList
   '''
  def setUp(self):
    self.url = reverse('listar-medicos')
    Medico(nome='aaa', crm=333, especialidade='ononononoon', telefone=2222, areamedica=3).save()

  def test_get(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(len(response.context.get('object_list')), 1)

class TestViewMedicosNew(TestCase):
  '''
  Classe de testes para a view MedicosNew
  '''
  def setUp(self):
    self.url = reverse('novo-medico')

  def test_get(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, 200)
    self.assertIsInstance(response.context.get('form'), FormularioMedico)

  def test_post(self):
    data = {'nome': 'aaa', 'crm': 333, 'especialidade': 'onononononon', 'telefone': 444, 'areamedica': 3}
    response = self.client.post(self.url, data)

    # Verifica se apos a insercao houve um redirecionamento para a view MedicosList
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('listar-medicos'))

    self.assertEqual(Medico.objects.count(), 1)
    self.assertEqual(Medico.objects.first().nome, 'aaa')

class TestViewMedicosEdit(TestCase):
  '''
  Classe de testes para a view MedicosEdit
  '''
  def setUp(self):
    self.instance = Medico.objects.create(nome='aaa', crm= 33, especialidade='onononon', telefone=233, areamedica=3)
    self.url = reverse('editar-medico', kwargs={'pk': self.instance.pk})

  def test_get(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, 200)
    self.assertIsInstance(response.context.get('object'), Medico)
    self.assertIsInstance(response.context.get('form'), FormularioMedico)
    self.assertEqual(response.context.get('object').pk, self.instance.pk)

  def test_post(self):
    data = {'nome': 'zzz', 'crm': 321, 'especialidade': 'onononononon', 'telefone': 2, 'areamedica': 2}
    response = self.client.post(self.url, data)
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('listar-medicos'))
    self.assertEqual(Medico.objects.count(), 1)
    self.assertEqual(Medico.objects.first().nome, 'zzz')
    self.assertEqual(Medico.objects.first().pk, self.instance.pk)

class TestViewMedicosDelete(TestCase):
  '''
  Classe de testes para a view MedicosDelete
  '''
  def setUp(self):
    self.instance = Medico.objects.create(nome='aaa', crm=324, especialidade='onononono', telefone=2212, areamedica=3)
    self.url = reverse('deletar-medico', kwargs={'pk': self.instance.pk})

  def test_get(self):
    response = self.client.get(self.url)
    self.assertEqual(response.status_code, 200)
    self.assertIsInstance(response.context.get('object'), Medico)
    self.assertEqual(response.context.get('object').pk, self.instance.pk)

  def test_post(self):
    response = self.client.post(self.url)

    # Verifica se apos a exclusao houve um redirecionamento para a view MedicosList
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, reverse('listar-medicos'))
    self.assertEqual(Medico.objects.count(), 0)


'''
----------------> Estes testes são referentes a campos com datas
#A linha abaixo é para incluir no cabeçalho
from datetime import datetime

class TestModelMedico(TestCase):
  '''
#  Classe de testes para o model Médico
  '''

  def setUp(self):
    self.instance = Médico(nome='aaa', crm=112, especialidade=datetime.now().year, telefone=2, areamedica=3)

  def test_is_new(self):
    self.assertTrue(self.instance.medico_novo)
    self.instance.especialidade = datetime.now().year – 5
    self.assertFalse(self.instance.medico_novo)

  def test_years_use(self):
    self.assertEqual(self.instance.anos_de_uso(), 0)
    self.instance.especialidade = datetime.now().year – 5
    self.assertEqual(self.instance.anos_de_uso(), 5)
'''
