from django.urls import path
from apps.products.api.views.general_views import MeasureUnitLIstAPIView, IndicatorLIstAPIView, \
    CategoryProductLIstAPIView
from apps.products.api.views.product_views import ProductListAPIview, ProductCreateAPIView, ProductRetrieveAPIView, \
    ProductDestroyAPIView, ProductUpdateAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitLIstAPIView.as_view(), name='measure_unit'),
    path('indicator/', IndicatorLIstAPIView.as_view(), name='indicartor'),
    path('category_product/', CategoryProductLIstAPIView.as_view(), name='category_product'),
    path('product/List/', ProductListAPIview.as_view(), name='product_list'),
    path('product/create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('product/retrieve/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('product/destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_destroy'),
    path('product/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
]
