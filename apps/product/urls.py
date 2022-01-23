from rest_framework import routers
from .views import ProductViewSet, CategoryViewSet
from django.urls import path, include

#creating routers
product_router = routers.SimpleRouter()
category_router = routers.SimpleRouter()

#registering viewsets for urls
product_router.register(r'products', ProductViewSet)
category_router.register(r'categories', CategoryViewSet)

urlpatterns = [ 
    path('', include(product_router.urls)),
    path('', include(category_router.urls)),
]

