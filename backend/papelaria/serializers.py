from rest_framework import serializers
from core.serializers import ProdutoSerializer
from .models import Papelaria
from core.models import Produto

class PapelariaSerializer(serializers.ModelSerializer):
    produto_detalhe = ProdutoSerializer(source='produto', read_only=True)

    produto = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all())

    class Meta:
        model = Papelaria
        fields = ['id', 'produto', 'produto_detalhe', 'marca', 'cor']
