from rest_framework import viewsets, status
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


class CategoryProductViewset(viewsets.GenericViewSet):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def get_object(self):
        return self.get_serializer().Meta.model.objects.filter(id=self.kwargs['pk'], state=True)

    def list(self, request):
        data = self.get_queryset()
        data = self.serializer_class(data, many=True)
        return Response(data.data)

    def create(self, requests):
        serializer = self.serializer_class(data=requests.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Categoria registrada correctamente'}, status=status.HTTP_201_CREATED)
        return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_object().exists():
            serializer = self.serializer_class(instance=self.get_object().get(), data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if self.get_object().exists():
            self.get_object().get().delete()
            return Response({'message': 'Categoria eliminada corectamente'}, status=status.HTTP_200_OK)
        return Response({'message': '', 'error': 'categoria no encontrada'})
