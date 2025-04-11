from django.db import models

# Create your models here.

from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome

class Destino(models.Model):
    cidade = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cidade}, {self.pais}"

class Transporte(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Viagem(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    transporte = models.ForeignKey(Transporte, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    data_viagem = models.DateField()

    def __str__(self):
        return f"{self.usuario.nome} - {self.destino} ({self.data_viagem})"
