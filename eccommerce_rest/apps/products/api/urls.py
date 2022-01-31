from django.urls import path
from apps.products.api.views.general_views import MeasureUnitViewset, IndicatorViewset, \
    CategoryProductViewset

urlpatterns = [
    path('measure_unit/', MeasureUnitViewset.as_view(), name='measure_unit'),
    path('indicator/', IndicatorViewset.as_view(), name='indicartor'),
]
