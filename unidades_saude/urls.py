from rest_framework.routers import DefaultRouter

from unidades_saude.views import UnidadeSaudeViewSet


router = DefaultRouter()
router.register(r'', UnidadeSaudeViewSet)

urlpatterns = router.urls