from django.urls import path
from apps.products.api.views.general_views import MeasureUnitLIstAPIView, IndicatorLIstAPIView, \
    CategoryProductLIstAPIView
from apps.products.api.views.product_views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitLIstAPIView.as_view(), name='measure_unit'),
    path('indicator/', IndicatorLIstAPIView.as_view(), name='indicartor'),
    path('category_product/', CategoryProductLIstAPIView.as_view(), name='category_product'),
    path('product/', ProductListCreateAPIView.as_view(), name='product_create_List'),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(),
         name='product_retrieve_update_destroy'),
]
