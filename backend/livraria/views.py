
# pyrefly: ignore [missing-import]
from rest_framework import viewsets

# Importa o model Produto.
# É a tabela do banco que essa ViewSet vai gerenciar.
from .models import Livro

# Importa o serializer que criamos em core/serializers.py.
# Ele é o "tradutor" que converte Produto ↔ JSON.
# Sem ele, a ViewSet não saberia como formatar os dados para a resposta.
from .serializers import LivroSerializer


# ProdutoViewSet herda de ModelViewSet.
#
# Por que ModelViewSet e não APIView ou ViewSet?
# O DRF oferece vários níveis de abstração:
#
#   APIView       → Mais controle, mais código. Você escreve get(), post() manualmente.
#   ViewSet       → Agrupa ações, mas sem implementação pronta.
#   ModelViewSet  → Tudo pronto: list, create, retrieve, update, destroy.
#
# Para um CRUD simples como o de Produtos, ModelViewSet é perfeito.
# Quando você precisar de lógica customizada (ex: o fluxo de venda do PDV),
# aí sim pode sobrescrever métodos específicos ou usar APIView.
class LivroViewSet(viewsets.ModelViewSet):

    # queryset define DE ONDE os dados vêm.
    # Produto.objects.all() significa "traga todos os produtos do banco".
    #
    # O .objects é o "Manager" do Django — o intermediário entre o Python e o SQL.
    # .all() gera internamente: SELECT * FROM core_produto;
    #
    # Se quiséssemos filtrar (ex: só produtos ativos), faríamos:
    #   queryset = Produto.objects.filter(ativo=True)
    # Mas por enquanto, queremos todos.
    queryset = Livro.objects.select_related('produto').all()

    # serializer_class define COMO os dados são traduzidos.
    # Quando alguém faz GET /api/produtos/, a ViewSet:
    #   1. Busca os dados usando o queryset acima
    #   2. Passa cada objeto Produto pelo ProdutoSerializer
    #   3. Retorna o JSON traduzido na resposta HTTP
    #
    # Quando alguém faz POST /api/produtos/ com um JSON no body,
    # o caminho é inverso:
    #   1. O ProdutoSerializer valida o JSON recebido
    #   2. Se válido, cria um objeto Produto no banco
    #   3. Retorna o produto criado como JSON na resposta
    serializer_class = LivroSerializer