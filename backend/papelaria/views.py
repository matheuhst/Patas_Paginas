from rest_framework import viewsets
from .models import Papelaria
from .serializers import PapelariaSerializer

class PapelariaViewSet(viewsets.ModelViewSet):
    queryset = Papelaria.objects.all()
    serializer_class = PapelariaSerializer
