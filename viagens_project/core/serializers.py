from rest_framework import serializers
from .models import Usuario, Destino, Transporte, Categoria, Viagem

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email'] 

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ['id', 'cidade', 'pais']  

class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = ['id', 'tipo']  

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']  

class ViagemSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()
    destino = DestinoSerializer()
    transporte = TransporteSerializer()
    categoria = CategoriaSerializer()

    class Meta:
        model = Viagem
        fields = ['id', 'usuario', 'destino', 'transporte', 'categoria', 'data_viagem']  # Campos específicos_
