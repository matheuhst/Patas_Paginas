from django.db import models

# Create your models here.
from django.db import models
from core.models import Produto

class Livro(models.Model):
    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='livro')
    isbn = models.CharField(max_length=20, unique=True)
    autor = models.CharField(max_length=255)
    editora = models.CharField(max_length=255)
    paginas = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.produto.nome} ({self.autor})"