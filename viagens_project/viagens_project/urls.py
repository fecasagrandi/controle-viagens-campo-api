from django.contrib import admin
from django.urls import path

from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', views.listarUsuarios, name='listar_usuarios'),
    path('usuarios/<int:pk>/', views.atualizarUsuario, name='atualizar_usuario'),
    path('usuarios/delete/<int:pk>/', views.deletarUsuario, name='deletar_usuario'),
    path('usuarios/inserir/', views.inserirUsuario, name='inserir_usuario'),

    path('destinos/', views.listarDestinos, name='listar_destinos'),
    path('destinos/<int:pk>/', views.atualizarDestino, name='atualizar_destino'),
    path('destinos/delete/<int:pk>/', views.deletarDestino, name='deletar_destino'),
    path('destinos/inserir/', views.inserirDestino, name='inserir_destino'),

    path('transportes/', views.listarTransportes, name='listar_transportes'),
    path('transportes/<int:pk>/', views.atualizarTransporte, name='atualizar_transporte'),
    path('transportes/delete/<int:pk>/', views.deletarTransporte, name='deletar_transporte'),
    path('transportes/inserir/', views.inserirTransporte, name='inserir_transporte'),

    path('categorias/', views.listarCategorias, name='listar_categorias'),
    path('categorias/<int:pk>/', views.atualizarCategoria, name='atualizar_categoria'),
    path('categorias/delete/<int:pk>/', views.deletarCategoria, name='deletar_categoria'),
    path('categorias/inserir/', views.inserirCategoria, name='inserir_categoria'),

    path('viagens/', views.listarViagens, name='listar_viagens'),
    path('viagens/<int:pk>/', views.atualizarViagem, name='atualizar_viagem'),
    path('viagens/delete/<int:pk>/', views.deletarViagem, name='deletar_viagem'),
    path('viagens/inserir/', views.inserirViagem, name='inserir_viagem'),
]

