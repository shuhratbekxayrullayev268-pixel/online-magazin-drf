from rest_framework.generics import ListAPIView
from api.user.serializers import category_serializers
from apps.shop.models import Product


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = category_serializers.ProductListSerializer

