from rest_framework.serializers import ModelSerializer
from apps.shop.models import Category




class CategoryListSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
