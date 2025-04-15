from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.viewsets import ModelViewSet  
from .pagination import CustomPagination

# Create your views here.
class AllProducViews(ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  

class ProducViews(ModelViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  pagination_class= CustomPagination
  
  
class CategoryView(ModelViewSet):
  queryset = Category.objects.all()
  serializer_class = CategorySerializer
  