"""
Passo 6 — Criar o Primeiro Serializer (O Tradutor)

Este arquivo existe porque o Django fala Python e o React fala JSON.
Alguém precisa traduzir entre os dois — esse é o papel do Serializer.

Ele faz duas coisas:
1. Serialização (Python → JSON):
   Pega um objeto Produto do banco e transforma em:
   {"nome": "1984", "sku": "LIV-001", "preco_venda": "39.90"}
   Isso acontece quando o frontend FAZ uma requisição GET.

2. Desserialização (JSON → Python):
   Pega o JSON enviado pelo frontend e transforma de volta
   num objeto Python validado, pronto para salvar no banco.
   Isso acontece quando o frontend ENVIA dados via POST ou PUT.

Por que este arquivo fica no core/?
Porque o model Produto vive no core. A regra é:
cada serializer fica na mesma app do model que ele traduz.
Isso mantém a organização modular — se amanhã o Produto mudar,
você sabe que o serializer dele está aqui do lado.
"""

# Importa o módulo de serializers do DRF (Django REST Framework).
# É daqui que vem o ModelSerializer — a classe base que sabe
# "ler" um Model do Django e gerar automaticamente os campos
# de tradução (string, número, data, etc.) sem você precisar
# declarar cada um manualmente.
# pyrefly: ignore [missing-import]
from rest_framework import serializers

# Importa o model Produto que criamos em core/models.py.
# O ponto (.) significa "do mesmo pacote" — ou seja, do próprio core.
# Sem esse import, o serializer não saberia qual tabela do banco traduzir.
from .models import Produto


# ProdutoSerializer herda de ModelSerializer.
#
# Por que ModelSerializer e não Serializer simples?
# Porque o ModelSerializer já faz o trabalho pesado:
#   - Lê os campos do Model automaticamente (nome, sku, preco_venda...)
#   - Gera validações automáticas (ex: sku unique=True vira validação de duplicata)
#   - Implementa create() e update() prontos para salvar no banco
#
# Se usássemos serializers.Serializer (sem o "Model"), teríamos que
# declarar cada campo manualmente:
#   nome = serializers.CharField(max_length=255)
#   sku = serializers.CharField(max_length=100)
#   ... campo por campo. Muito mais código, muito mais chance de erro.
class ProdutoSerializer(serializers.ModelSerializer):

    # class Meta é uma classe interna de configuração.
    # Ela diz ao ModelSerializer QUAL model traduzir e QUAIS campos incluir.
    # Sem ela, o serializer não sabe o que fazer — daria erro.
    class Meta:

        # model = Produto → "Este serializer traduz a tabela Produto."
        # É aqui que o DRF sabe de onde puxar os campos.
        model = Produto

        # fields = '__all__' → "Inclua TODOS os campos do model na tradução."
        # Isso significa que o JSON vai conter: id, nome, sku, preco_venda,
        # preco_custo, estoque, tipo, is_composicao, criado_em.
        #
        # ⚠️ CUIDADO EM PRODUÇÃO: '__all__' é prático para aprendizado,
        # mas perigoso no mundo real. Se amanhã você adicionar um campo
        # sensível (ex: senha_hash, margem_lucro), ele apareceria na API
        # pública automaticamente sem você perceber.
        #
        # A boa prática profissional é listar explicitamente:
        # fields = ['id', 'nome', 'sku', 'preco_venda', 'tipo', 'estoque']
        # Assim você controla exatamente o que sai e o que fica escondido.
        fields = '__all__'