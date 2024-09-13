from rest_framework import serializers

from .models import Brand, Category, Product

class BrandSerializer(serializers.ModelSerializer):
    class Meta():
        model = Brand
        fields = '__all__'

# {"name" : Brand.name}

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ["id", "name", "parent"]

class ProductSerializer(serializers.ModelSerializer):
    Brand = BrandSerializer()
    Category = CategorySerializer()

    class Meta():
        model = Product
        fields = '__all__'