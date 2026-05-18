from rest_framework.routers import DefaultRouter
from .views import PapelariaViewSet

router = DefaultRouter()
# Registra a rota raiz (/) para o PapelariaViewSet
router.register(r'produtos/papelaria', PapelariaViewSet, basename='papelaria')

urlpatterns = router.urls
