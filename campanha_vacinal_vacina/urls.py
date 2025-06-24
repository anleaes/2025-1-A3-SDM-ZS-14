from rest_framework.routers import DefaultRouter

from campanha_vacinal_vacina.views import CampanhaVacinalVacinaViewSet

router = DefaultRouter()
router.register(r'', CampanhaVacinalVacinaViewSet)

urlpatterns = router.urls