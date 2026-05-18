<<<<<<< HEAD
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
=======

# pyrefly: ignore [missing-import]
from rest_framework import serializers
from .models import Livro
from core.serializers import ProdutoSerializer
from core.models import Produto

class LivroSerializer(serializers.ModelSerializer):
    produto_detalhe = ProdutoSerializer(source='produto', read_only=True)
    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())

    class Meta:
        model = Livro
        fields = ['id', 'produto', 'produto_detalhe', 'isbn', 'autor', 'editora', 'paginas' ]
>>>>>>> eff2be4fc3a68b42c9554a740da127444faa6e37
