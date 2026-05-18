"""
Passo 8 — Conectar as URLs (O Roteador)

Este arquivo existe porque o Django precisa saber:
"Quando alguém acessar /api/livros/, qual código deve responder?"

Sem este arquivo, seus Serializers e ViewSets existem mas são invisíveis —
ninguém consegue acessá-los pela web. É como ter uma loja montada
mas sem porta de entrada.
"""
# DefaultRouter é um "gerador automático de URLs" do DRF(Django Rest Framework).
# Ele olha pra uma ViewSet e cria sozinho todas as rotas REST:
#   GET    /produtos/     → lista todos os produtos
#   POST   /produtos/     → cria um novo produto
#   GET    /produtos/1/   → detalha o produto com id=1
#   PUT    /produtos/1/   → edita o produto com id=1
#   DELETE /produtos/1/   → apaga o produto com id=1
# Sem o Router, você teria que escrever cada uma dessas 5 rotas manualmente.
# pyrefly: ignore [missing-import]
from rest_framework.routers import DefaultRouter

# Importa a ViewSet que criamos em livraria/views.py.
# O ponto (.) significa "do mesmo pacote/app" — ou seja, da própria livraria.
from .views import LivroViewSet

# Cria uma instância do Router.
# Pense nele como um "despachante" que vai organizar todas as rotas da app core.
router = DefaultRouter()

# Registra a ProdutoViewSet no router.
# O primeiro argumento r'livros' é o prefixo da URL.
# Como no patas_paginas/urls.py nós já definimos path('api/', include('livraria.urls')),
# a URL final será: /api/ + livros/ = /api/livros/
#
# O r'' antes da string significa "raw string" — diz ao Python para não interpretar
# caracteres especiais como \n. É uma boa prática em padrões de URL.
#
# Nota: NÃO usamos basename='livro' aqui porque a ViewSet já tem
# queryset = Livro.objects.all() definido. O DRF infere o nome automaticamente.
# O basename só é necessário quando a ViewSet não tem queryset (casos avançados).
router.register(r'livros', LivroViewSet)

# Esta é a linha mais importante do arquivo.
# O Django, ao carregar qualquer arquivo de URLs, procura uma variável chamada
# exatamente "urlpatterns". Se ela não existir, o Django não sabe quais rotas servir.
#
# router.urls contém a lista de todas as rotas que o router gerou automaticamente
# a partir das ViewSets registradas acima.
#
# Sem esta linha, o router cria as rotas internamente mas ninguém as encontra —
# é como ter um cardápio pronto mas não entregar pro garçom.
urlpatterns = router.urls
