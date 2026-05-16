# pyrefly: ignore [missing-import]
from core.serializers import ProdutoSerializer

# pyrefly: ignore [missing-import]
from rest_framework import serializers
from .models import CafeInsumo, ReceitaDiretaAoCliente, ReceitaItem

class CafeInsumoSerializer(serializers.ModelSerializer):
    produto_detalhe = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta: 
        model = CafeInsumo
        fields = '__all__'
        read_only_fields = ('produto','produto_detalhe', 'unidade', 'data_validade', )

class ReceitaItemSerializer(serializers.ModelSerializer):
    insumo = serializers.PrimaryKeyRelatedField(read_only=True)
    insumo_detalhe = ProdutoSerializer(source='insumo', read_only=True)
    class Meta: 
        model = ReceitaItem
        fields = '__all__'
        read_only_fields = ('insumo','insumo_detalhe', 'receita', 'receita' )
    
class ReceitaDiretaAoClienteSerializer(serializers.ModelSerializer):
    receita_detalhe = ReceitaItemSerializer(source='receita', read_only=True)
    class Meta: 
        model = ReceitaDiretaAoCliente
        fields = '__all__'
        read_only_fields = ('receita_detalhe','produto_final', 'descricao' )