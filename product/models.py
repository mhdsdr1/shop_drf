from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Brand (models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)

    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Category = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
