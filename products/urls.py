from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import ProducViews, CategoryView

# Create a router instance
router = DefaultRouter()  
router.register(r'products', ProducViews, basename='product')  
router.register(r'category', CategoryView, basename='categories')  

urlpatterns = [
  path('', include(router.urls)),  
]
