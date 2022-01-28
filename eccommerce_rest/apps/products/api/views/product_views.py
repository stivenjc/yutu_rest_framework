from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.products.api.serialializers.product_serializers import ProductSerializer


# list con class
class ProductListAPIview(GeneralListApiView):
    serializer_class = ProductSerializer


# create con class
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesage': 'product creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# listar un solo objects con class
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)


# eliminar un solo objec con class
class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)

    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'mesage': 'product eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'no existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
