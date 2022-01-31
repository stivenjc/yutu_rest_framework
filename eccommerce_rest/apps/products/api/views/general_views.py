from rest_framework import viewsets
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.api.serialializers.general_serializers import MeasureUNitSerializer, IndicatorSerializer, \
    CategoryProductSerializer
from apps.products.models import MeasureUnit


class MeasureUnitViewset(viewsets.ModelViewSet):
    """
    hola desde la ruta como tal.
    """
    model = MeasureUnit
    serializer_class = MeasureUNitSerializer

    def queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def list(self):
        """
        list


        paramet.

        """
        data = self.get_queryset()
        data = self.get_serializ(data, many=True)
        return Response(data.data)


class IndicatorViewset(viewsets.ModelViewSet):
    serializer_class = IndicatorSerializer


class CategoryProductViewset(viewsets.ModelViewSet):
    serializer_class = CategoryProductSerializer
