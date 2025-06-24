from rest_framework.routers import DefaultRouter

from vacinas.views import VacinaViewSet


router = DefaultRouter()
router.register(r'', VacinaViewSet)

urlpatterns = router.urls