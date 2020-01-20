from django.shortcuts import render
from .models import *
from usuario.forms import PessoaForm

# Create your views here.


def mostrar_formulario_cadastro(request):
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
    if pessoa_banco_dados is not 
    :
      return mostrar_pessoas(request)
    return render(request, 'login.html', {'msg': 'Ops, não encontramos'}) 

  return render(request, 'login.html', {'msg': 'seja bem vindo'})

  def atualizar_pessoa(request, id):
    pessoa = Pessoa.objects.get(pk=id)

    form = PessoaForm(request.POST or None, instance=pessoa)

    
    args = {'form':form}
    
    if form.is_valid():
        form.save()
        args = {
            'msg':'Cadastro atulizado com sucesso'
        }
    return render(request, 'atualizarpessoa.html', args)

def deletar_pessoa(request, id):
    pessoa = pessoa.objects.get(pk=id)

    pessoa.delete()

    args = {
        'msg':'a pessoa foi deletada com sucesso',
        pessoa':pessoa
        }
    return render(request, 'deletar_pessoa.html', args)
