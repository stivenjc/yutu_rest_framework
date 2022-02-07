from rest_framework import viewsets
from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.response import Response
from apps.products.api.serialializers.product_serializers import ProductSerializer


# creando nuestro primer viewsets
class ProductViewsets(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    parser_classes = (JSONParser, MultiPartParser)

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        product_serializers = self.get_serializer(self.get_queryset(), many=True)
        return Response(product_serializers.data, status=status.HTTP_200_OK)

    def create(self, request):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mesage': 'product creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_200_OK)
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'mesage': 'product eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'no existe un producto con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
