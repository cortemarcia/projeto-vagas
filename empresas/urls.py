from django.urls import path
from empresas.views import *

urlpatterns = [
    path('',home),
    path('cadastro/', cadastrar_empresa),
    path ('lista/', lista_empresas),
    path ('descricao/<int:id>', detalhes_empresa),
    path('atualizar/<int:id>', atualizar_empresa),
    path('deletar/<int:id>', deletar_empresa),
    
]