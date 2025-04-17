from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Usuario, Destino, Transporte, Categoria, Viagem
import re, datetime


# Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Usuario.objects.all())]
    )

    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email']

    def validate_email(self, value):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', value):
            raise serializers.ValidationError("Formato de e-mail inválido.")
        return value

# Destino
class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ['id', 'cidade', 'pais']

    def validate(self, data):
        if data['cidade'] == data['pais']:
            raise serializers.ValidationError("Cidade e País não podem ser iguais.")
        return data

# Transporte
class TransporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transporte
        fields = ['id', 'tipo']

# Categoria
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nome']

# Viagem
class ViagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viagem
        fields = ['id', 'usuario', 'destino', 'transporte', 'categoria', 'data_viagem']

    def validate_data_viagem(self, value):
        if value < datetime.date.today():
            raise serializers.ValidationError("A data da viagem não pode ser no passado.")
        return value

