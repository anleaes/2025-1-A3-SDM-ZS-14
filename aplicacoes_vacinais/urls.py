from rest_framework.routers import DefaultRouter

from aplicacoes_vacinais.views import AplicacaoVacinaViewSet


router = DefaultRouter()
router.register(r'', AplicacaoVacinaViewSet)

urlpatterns = router.urls