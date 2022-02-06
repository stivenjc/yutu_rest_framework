from rest_framework.routers import DefaultRouter

from apps.products.api.views.general_views import *
from apps.products.api.views.product_viewsets import ProductViewsets

# solo ruatas que tengas(viewsets.--)
router = DefaultRouter()
router.register(r'products', ProductViewsets, basename='prducts')
router.register(r'measure-unit', MeasureUnitViewset, basename='measure-unit')
router.register(r'indicator', IndicatorViewset, basename='indicator')
router.register(r'category-product', CategoryProductViewset, basename='category-products')
urlpatterns = router.urls
