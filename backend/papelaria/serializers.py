from rest_framework import serializers
from core.serializers import ProdutoSerializer
from .models import Papelaria

class PapelariaSerializer(serializers.ModelSerializer):
    # O ProdutoSerializer traz as informações base (nome, preco)
    produto = ProdutoSerializer()

    class Meta:
        model = Papelaria
        fields = '__all__'
