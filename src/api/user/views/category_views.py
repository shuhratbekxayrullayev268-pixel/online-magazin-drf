from rest_framework.generics import ListAPIView
from api.user.serializers import category_serializers
from apps.shop.models import Category


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = category_serializers.CategoryListSerializer

