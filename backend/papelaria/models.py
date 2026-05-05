from django.db import models
from core.models import Produto

class Papelaria(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='papelaria')
    marca = models.CharField(max_length=100)
    cor = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.produto.nome} ({self.marca})"