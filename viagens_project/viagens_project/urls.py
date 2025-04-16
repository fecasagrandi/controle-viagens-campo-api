from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Usuário
    path('usuarios/', views.listarUsuarios, name='listar_usuarios'),
    path('usuarios/inserir/', views.inserirUsuario, name='inserir_usuario'),
    path('usuarios/<int:pk>/', views.atualizarUsuario, name='atualizar_usuario'),
    path('usuarios/delete/<int:pk>/', views.deletarUsuario, name='deletar_usuario'),

    # Destino
    path('destinos/', views.listarDestinos, name='listar_destinos'),
    path('destinos/inserir/', views.inserirDestino, name='inserir_destino'),
    path('destinos/<int:pk>/', views.atualizarDestino, name='atualizar_destino'),
    path('destinos/delete/<int:pk>/', views.deletarDestino, name='deletar_destino'),

    # Transporte
    path('transportes/', views.listarTransportes, name='listar_transportes'),
    path('transportes/inserir/', views.inserirTransporte, name='inserir_transporte'),
    path('transportes/<int:pk>/', views.atualizarTransporte, name='atualizar_transporte'),
    path('transportes/delete/<int:pk>/', views.deletarTransporte, name='deletar_transporte'),

    # Categoria
    path('categorias/', views.listarCategorias, name='listar_categorias'),
    path('categorias/inserir/', views.inserirCategoria, name='inserir_categoria'),
    path('categorias/<int:pk>/', views.atualizarCategoria, name='atualizar_categoria'),
    path('categorias/delete/<int:pk>/', views.deletarCategoria, name='deletar_categoria'),

    # Viagem
    path('viagens/', views.listarViagens, name='listar_viagens'),
    path('viagens/inserir/', views.inserirViagem, name='inserir_viagem'),
    path('viagens/<int:pk>/', views.atualizarViagem, name='atualizar_viagem'),
    path('viagens/delete/<int:pk>/', views.deletarViagem, name='deletar_viagem'),
]

