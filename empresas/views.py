from django.shortcuts import render
from empresas.models import *
from empresas.forms import EmpresaForm
# Create your views here.
<<<<<<< HEAD

=======
# teste:
>>>>>>> 6b77e7a576968912e0fc6ffb54681d7d5a4a77c2

def home(request):
    return render(request,'base.html')

def cadastrar_empresa(request):
    
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        args = {
            'form':form, 
            'msg':'O cadastro foi realizado com sucesso :)'
        }
        return render(request, 'cadastro.html', args)
    args= {'form':form}  
    return render(request, 'cadastro.html', args)

def lista_empresas(request):
     lista_empresas = Empresa.objects.filter().all()
     args = {'lista_empresas':lista_empresas}
     return render(request, 'listadeempresas.html',args)

def detalhes_empresa(request, id):
    empresa= Empresa.objects.get(pk=id)
    
    args={'empresa':empresa}
    return render(request, 'detalhes.html',args)



def atualizar_empresa(request, id):
    empresa= Empresa.objects.get(pk=id)
    form = EmpresaForm(request.POST or None, instance= empresa)

    args= { 'form':form}

    if form.is_valid():
        form.save()
        args = {
    
            'msg':'O cadastro foi atualizado com sucesso :)'
        }
    return render(request, 'atualizarempresa.html',args)

def deletar_empresa(request, id):
    empresa= Empresa.objects.get(pk=id)
    empresa.delete()
    args = {  
            'msg':'O cadastro foi deletado com sucesso :)',
            'empresa': empresa
        }
    return render(request,'detalhes.html',args)  




