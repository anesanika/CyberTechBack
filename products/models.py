from django.db import models
  

class Category(models.Model):
  title = models.CharField(max_length=66)
  def __str__(self):
    return self.title
    

class Product(models.Model):
  title = models.CharField(max_length=122)
  descriptions = models.TextField(null=True)
  price = models.IntegerField(default=0)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
  def __str__(self):
    return self.title

class ProductImage(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
  image = models.ImageField(upload_to="product_images/")
  def __str__(self):
    return f"Image for {self.product.title}"  