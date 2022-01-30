from django.urls import path
from apps.products.api.views.general_views import MeasureUnitLIstAPIView, IndicatorLIstAPIView, \
    CategoryProductLIstAPIView

urlpatterns = [
    path('measure_unit/', MeasureUnitLIstAPIView.as_view(), name='measure_unit'),
    path('indicator/', IndicatorLIstAPIView.as_view(), name='indicartor'),
]
