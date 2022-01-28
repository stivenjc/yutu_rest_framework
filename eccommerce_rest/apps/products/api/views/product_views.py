from apps.base.api import GeneralListApiView
from apps.products.api.serialializers.product_serializers import ProductSerializer


class ProductListAPIview(GeneralListApiView):
    serializer_class = ProductSerializer