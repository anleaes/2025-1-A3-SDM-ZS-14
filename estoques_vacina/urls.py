from rest_framework.routers import DefaultRouter

from estoques_vacina.views import EstoqueVacinaViewSet


router = DefaultRouter()
router.register(r'', EstoqueVacinaViewSet)

urlpatterns = router.urls