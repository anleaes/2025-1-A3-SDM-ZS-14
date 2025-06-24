from rest_framework.routers import DefaultRouter

from medicos.views import MedicoViewSet

router = DefaultRouter()
router.register(r'', MedicoViewSet)

urlpatterns = router.urls