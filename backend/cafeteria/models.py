from django.db import models
from core.models import Produto


class CafeInsumo(models.Model):
    """
    Extensão de Produto para insumos perecíveis da cafeteria.
    Ex: Leite (ml), Pó de Café (g), Copos descartáveis (un).
    Estes itens NÃO são vendidos diretamente ao cliente — são consumidos pelas receitas.
    """
    class UnidadeMedida(models.TextChoices):
        GRAMAS = 'g', 'Gramas'
        MILILITROS = 'ml', 'Mililitros'
        UNIDADE = 'un', 'Unidade'

    produto = models.OneToOneField(Produto, on_delete=models.CASCADE, related_name='cafe_insumo')
    unidade = models.CharField(max_length=2, choices=UnidadeMedida.choices)
    data_validade = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.produto.nome} ({self.unidade})"


class ReceitaDiretaAoCliente(models.Model):
    """
    Representa um produto composto vendido ao cliente.
    Ex: "Café Expresso", "Café Macchiato".
    O produto_final aponta para um Produto com is_composicao=True.
    """
    produto_final = models.OneToOneField(
        Produto,
        on_delete=models.CASCADE,
        related_name='receita',
        limit_choices_to={'is_composicao': True}
    )
    descricao = models.TextField(blank=True)

    def __str__(self):
        return f"Receita: {self.produto_final.nome}"


class ReceitaItem(models.Model):
    """
    Cada linha de ingrediente de uma receita.
    Ex: Receita "Café Macchiato" usa:
      - 15g de Pó de Café  → ReceitaItem(receita=macchiato, insumo=po_cafe, quantidade=15)
      - 50ml de Leite      → ReceitaItem(receita=macchiato, insumo=leite, quantidade=50)
    Ao vender 1 Macchiato, o sistema percorre esses itens e abate do estoque de cada insumo.
    """
    receita = models.ForeignKey(ReceitaDiretaAoCliente, on_delete=models.CASCADE, related_name='itens')
    insumo = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='usado_em_receitas')
    quantidade = models.DecimalField(max_digits=8, decimal_places=3)

    def __str__(self):
        return f"{self.quantidade} de {self.insumo.nome} → {self.receita.produto_final.nome}"
