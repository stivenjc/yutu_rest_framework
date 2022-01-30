from rest_framework.routers import DefaultRouter

from apps.products.api.views.product_viewsets import ProductViewsets

router = DefaultRouter()
router.register(r'products', ProductViewsets, basename='prducts')
urlpatterns = router.urls
