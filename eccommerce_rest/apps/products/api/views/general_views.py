from apps.base.api import GeneralListApiView
from apps.products.api.serialializers.general_serializers import MeasureUNitSerializer, IndicatorSerializer, \
    CategoryProductSerializer


class MeasureUnitLIstAPIView(GeneralListApiView):
    serializer_class = MeasureUNitSerializer


class IndicatorLIstAPIView(GeneralListApiView):
    serializer_class = IndicatorSerializer


class CategoryProductLIstAPIView(GeneralListApiView):
    serializer_class = CategoryProductSerializer

