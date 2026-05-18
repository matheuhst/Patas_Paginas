# pyrefly: ignore [missing-import]
from rest_framework.routers import DefaultRouter
from .views import CafeInsumoViewSet, ReceitaItemViewSet, ReceitaDiretaAoClienteViewSet

router = DefaultRouter()
router.register(r'cafeinsumos', CafeInsumoViewSet)
router.register(r'receitaitens', ReceitaItemViewSet)
router.register(r'receitas', ReceitaDiretaAoClienteViewSet)
urlpatterns = router.urls