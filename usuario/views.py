from django.shortcuts import render
from .models import *
from usuario.forms import PessoaForm

# Create your views here.


def mostrar_formulario_cadastro(request):
  # args = {'msg': ''}
  # if request == 'POST':
  #   pessoa = Pessoa()
  #   pessoa.nome = request.POST.get('nome')
  #   pessoa.cpf = request.POST.get('cpf')
  #   pessoa.email = request.POST.get('email')
  #   pessoa.telefone = request.POST.get('telefone')
  #   pessoa.genero = request.POST.get('genero')
  #   pessoa.save
  #   return render(request, 'login.html')
  # return render(request, 'cadastrar_pessoa.html', args)

  form = PessoaForm(request.POST or None)
  if form.is_valid():
     form.save()
     return redirect('/login', kwargs={'msg':'Cadastrado com sucesso'})

  usuarios = reversed(Pessoa.objects.filter().all())

  args = {
      'usuarios': usuarios,
      'form':form
  }

  return render(request, 'cadastrar_pessoa.html', args)


def mostrar_pessoas(request):
  pessoas = Pessoa.objects.all()
  return render(request, 'pessoas.html', {'dados': pessoas})

def login(request):
  if request.method == 'POST':
    email_formulario = request.POST.get('email')
    pessoa_banco_dados = Pessoa.objects.filter(email=email_formulario).first()
    if pessoa_banco_dados is not None:
      return mostrar_pessoas(request)
    return render(request, 'login.html', {'msg': 'Ops, não encontramos'})

  return render(request, 'login.html', {'msg': 'seja bem vindo'})