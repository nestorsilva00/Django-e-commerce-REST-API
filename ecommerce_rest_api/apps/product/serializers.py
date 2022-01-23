from xml.etree.ElementInclude import include
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Category, Product, Product_Image


class CategorySerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)

    class Meta:
        depth = 1
        model = Category
        exclude = ['deleted_at']
      
        

class ProductSerializer(ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=500)
    SKU = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=5, decimal_places=2)
    created_at = serializers.DateTimeField(read_only=True)
    modified_at = serializers.DateTimeField(read_only=True)
    

    class Meta:
        depth = 1
        model = Product
        #exclude = ['deleted_at']
        fields = ['id','name','description','SKU','price','created_at', 'modified_at', 'product_image','category_id']
    

class ProductImageSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    product_id=ProductSerializer(read_only=True)
    image=serializers.ImageField()
    description=serializers.CharField(max_length=150)
    color=serializers.CharField(max_length=20)

    class Meta:
        model = Product_Image
        exclude = ['deleted_at']