from rest_framework import serializers
from .models import Usuario, Destino, Transporte, Categoria, Viagem

class UsuarioSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'  

class DestinoSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__' 

class TransporteSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = '__all__'

class CategoriaSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ViagemSerializerAll(serializers.ModelSerializer):
    usuario = UsuarioSerializerAll()
    destino = DestinoSerializerAll()
    transporte = TransporteSerializerAll()
    categoria = CategoriaSerializerAll()

    class Meta:
        model = Viagem
        fields = '__all__'
