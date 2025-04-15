from django.urls import path, include  
from rest_framework.routers import DefaultRouter  
from .views import ProducViews, CategoryView, AllProducViews

# Create a router instance
router = DefaultRouter()  
router.register(r'products', ProducViews, basename='product')  
router.register(r'allproducts', AllProducViews, basename='AllProduct')  
router.register(r'category', CategoryView, basename='categories')  

urlpatterns = [
  path('', include(router.urls)),  
]
