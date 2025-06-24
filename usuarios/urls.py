from rest_framework.routers import DefaultRouter

from usuarios.views import UsuarioViewSet


router = DefaultRouter()
router.register(r'', UsuarioViewSet)

urlpatterns = router.urls