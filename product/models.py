from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class ActiveQuerySet(models.QuerySet):
    def isactive (self):
        return self.filter(is_active = True)
    

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
    is_active = models.BooleanField(default=True)

    Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    Category = TreeForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)

    objects = ActiveQuerySet.as_manager()

    def __str__(self):
        return self.name


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sku = models.CharField(max_length=100)
    stock_qty = models.IntegerField()
    is_active = models.BooleanField(default=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "product_line")

    objects = ActiveQuerySet.as_manager()

