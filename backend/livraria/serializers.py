# pyrefly: ignore [missing-import]
from rest_framework import serializers
from .models import Livro
from core.serializers import ProdutoSerializer
from core.models import Produto

class LivroSerializer(serializers.ModelSerializer):
    # Usamos o ProdutoSerializer como read_only para trazer os detalhes do produto,
    # e PrimaryKeyRelatedField para permitir a associação do produto na criação via ID.
    produto_detalhe = ProdutoSerializer(source='produto', read_only=True)
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())

    class Meta:
        model = Livro
        fields = ['id', 'produto', 'produto_detalhe', 'isbn', 'autor', 'editora', 'paginas']
