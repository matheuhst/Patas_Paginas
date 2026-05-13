"""
Passo 7 — Criar a Primeira View de API (O Controlador)

Este arquivo é o "cérebro" da API. Ele decide O QUE ACONTECE quando
alguém faz uma requisição para /api/produtos/.

No Django puro (sem DRF), uma "view" é uma função que recebe um request
e retorna um response. Você teria que escrever uma função para listar,
outra para criar, outra para editar, outra para deletar...

Com o DRF, uma ViewSet faz tudo isso numa única classe.
É como ter 5 funcionários num único empregado.
"""

# Importa o módulo viewsets do DRF.
# viewsets.ModelViewSet é a classe que dá o CRUD completo de graça:
#   - list()    → GET /produtos/      → Lista todos
#   - create()  → POST /produtos/     → Cria novo
#   - retrieve()→ GET /produtos/1/    → Detalha um
#   - update()  → PUT /produtos/1/    → Edita um
#   - destroy() → DELETE /produtos/1/ → Apaga um
#
# Todas essas 5 ações já vêm implementadas. Você só precisa dizer
# DE ONDE buscar os dados (queryset) e COMO traduzi-los (serializer).
# pyrefly: ignore [missing-import]
from rest_framework import viewsets

# Importa o model Produto.
# É a tabela do banco que essa ViewSet vai gerenciar.
from .models import Produto

# Importa o serializer que criamos em core/serializers.py.
# Ele é o "tradutor" que converte Produto ↔ JSON.
# Sem ele, a ViewSet não saberia como formatar os dados para a resposta.
from .serializers import ProdutoSerializer


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
class ProdutoViewSet(viewsets.ModelViewSet):

    # queryset define DE ONDE os dados vêm.
    # Produto.objects.all() significa "traga todos os produtos do banco".
    #
    # O .objects é o "Manager" do Django — o intermediário entre o Python e o SQL.
    # .all() gera internamente: SELECT * FROM core_produto;
    #
    # Se quiséssemos filtrar (ex: só produtos ativos), faríamos:
    #   queryset = Produto.objects.filter(ativo=True)
    # Mas por enquanto, queremos todos.
    queryset = Produto.objects.all()

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
    serializer_class = ProdutoSerializer