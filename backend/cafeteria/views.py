# pyrefly: ignore [missing-import]
from rest_framework import viewsets
from .models import CafeInsumo, ReceitaDiretaAoCliente, ReceitaItem
from .serializers import CafeInsumoSerializer, ReceitaDiretaAoClienteSerializer, ReceitaItemSerializer


class CafeInsumoViewSet(viewsets.ModelViewSet):
    """
    View para gerenciar Insumos (Café, Leite, Açúcar, etc)
    """
    queryset = CafeInsumo.objects.all()
    serializer_class = CafeInsumoSerializer


class ReceitaDiretaAoClienteViewSet(viewsets.ModelViewSet):
    """
    View para gerenciar Receitas (Café Expresso, Cappuccino, etc)
    """
    queryset = ReceitaDiretaAoCliente.objects.all()
    serializer_class = ReceitaDiretaAoClienteSerializer


class ReceitaItemViewSet(viewsets.ModelViewSet):
    """
    View para gerenciar Itens de Receitas (Ingredientes)
    """
    queryset = ReceitaItem.objects.all()
    serializer_class = ReceitaItemSerializer
    
