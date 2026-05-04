from django.db import models

# Create your models here.
class TipoProduto(models.TextChoices):
    LIVRO = 'livro', 'Livraria'
    PAPELARIA = 'papelaria', 'Papelaria'
    CAFE_INSUMO = 'cafe_insumo', 'Insumo de Café'
    CAFE_RECEITA = 'cafe_receita', 'Receita de Café'
    CAFE_DIRETO = 'cafe_direto', 'Venda Direta de Café'

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    sku = models.CharField(max_length=100, unique=True)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.DecimalField(max_digits=10, decimal_places=3)
    tipo = models.CharField(max_length=20, choices=TipoProduto.choices)
    is_composicao = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome