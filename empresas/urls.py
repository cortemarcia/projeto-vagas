from django.urls import path
from empresas.views import *

urlpatterns = [
    path('',home),
    path('cadastro/', cadastrar_empresa),
    path ('lista/empresa/', lista_empresas),
    path ('empresa/<int:id>', detalhes_empresa),
    path('update/<int:id>', atualizar_empresa),
    path('delete/<int:id>', deletar_empresa),
    
]