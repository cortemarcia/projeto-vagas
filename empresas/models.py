from django.db import models

# Create your models here.
class Empresa(models.Model):
  
  nome = models.CharField(max_length=255, verbose_name='Nome')
  endereco= models.CharField(max_length=255)
  cnpj = models.CharField(max_length=255, verbose_name='CPF')
  telefone= models.CharField(max_length=255)
  email = models.EmailField(max_length=255, verbose_name='E-mail')
  quantidade_de_vagas= models.IntegerField()
  cargo= models.CharField(max_length=255)
  descricao_da_vaga= models.CharField(max_length=255)

  def __str__(self):
    return self.nome
