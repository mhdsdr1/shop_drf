from django.contrib import admin
from .models import Brand, Product, Category

# Register your models here.

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)