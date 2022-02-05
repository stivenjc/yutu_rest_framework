from rest_framework.routers import DefaultRouter
from apps.users.api.api import UserViewSet

# solo ruatas que tengas(viewsets.--)

router = DefaultRouter()
router.register(r'', UserViewSet, basename='user')
urlpatterns = router.urls
