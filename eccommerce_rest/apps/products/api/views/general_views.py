from rest_framework import generics

from apps.products.models import MeasureUnit, Indicator, CategoryProduct
from apps.products.api.serialializers.general_serializers import MeasureUNitSerializer, IndicatorSerializer, \
    CategoryProductSerializer


class MeasureUnitLIstAPIView(generics.ListAPIView):
    serializer_class = MeasureUNitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(state=True)


class IndicatorLIstAPIView(generics.ListAPIView):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return Indicator.objects.filter(state=True)


class CategoryProductLIstAPIView(generics.ListAPIView):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return CategoryProduct.objects.filter(state=True)
