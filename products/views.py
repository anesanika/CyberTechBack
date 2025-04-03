from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.viewsets import ModelViewSet  

# Create your views here.
class ProducViews(ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  
  
class CategoryView(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  