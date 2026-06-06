from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.user.views.category_views import CategoryListAPIView
from api.user.views.product_views import ProductListAPIView




router = DefaultRouter()
router.include_root_view = False

urlpatterns = [

        path('categories/', CategoryListAPIView.as_view()), 
        path('products/', ProductListAPIView.as_view()), 

    # path('', include(router.urls)),
    # path('restaurant/', RestaurantViewset.as_view({'get': 'list','post':'create'}), name='restaurant-detail'),
]

