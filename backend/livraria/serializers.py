from rest_framework import serializers
from core.serializers import ProdutoSerializer
from .models import Livro

class LivroSerializer(serializers.ModelSerializer):
    # Como Livro tem uma relação OneToOne com Produto, nós embutimos o
    # ProdutoSerializer aqui para que a API retorne os dados do produto (nome, preço)
    # junto com os dados específicos do livro (isbn, autor).
    produto = ProdutoSerializer()

    class Meta:
        model = Livro
        fields = '__all__'
