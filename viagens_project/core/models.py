from django.db import models
from django.core.exceptions import ValidationError
import re

# Usuario
class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def clean(self):
        if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', self.email):
            raise ValidationError({'email': 'Formato de e-mail inválido'})

    def __str__(self):
        return self.nome

# Destino
class Destino(models.Model):
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def clean(self):
        if self.cidade == self.pais:
            raise ValidationError("Cidade e País não podem ser iguais.")

    def __str__(self):
        return f"{self.cidade}, {self.pais}"

# Transporte
class Transporte(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

# Categoria
class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

# Viagem
class Viagem(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_viagem = models.DateField()

    def __str__(self):
        return f"{self.usuario.nome} - {self.destino} ({self.data_viagem})"
