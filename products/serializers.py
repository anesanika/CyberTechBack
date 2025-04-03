
from rest_framework import serializers  
from .models import Product, ProductImage, Category

class CategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = Category
    fields = "__all__"

    
class ProductImageSerialzer(serializers.ModelSerializer):
  class Meta:
    model = ProductImage
    fields = ["id", "image"]


class ProductSerializer(serializers.ModelSerializer):
  images = ProductImageSerialzer(many=True, read_only=True)
  category = serializers.CharField(source="category.title", read_only=True)

  class Meta:
    model = Product
    fields = ["id", "title", "descriptions", "price", "category", "images"]

