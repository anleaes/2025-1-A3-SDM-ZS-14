from rest_framework.routers import DefaultRouter

from campanhas_vacinais.views import CampanhaVacinalViewSet


router = DefaultRouter()
router.register(r'', CampanhaVacinalViewSet)

urlpatterns = router.urls