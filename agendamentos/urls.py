from rest_framework.routers import DefaultRouter

from agendamentos.views import AgendamentoViewSet

router = DefaultRouter()
router.register(r'', AgendamentoViewSet)

urlpatterns = router.urls