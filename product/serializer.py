from rest_framework import serializers

from .models import Brand, Category, Product, ProductLine

class BrandSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source="name")
    class Meta():
        model = Brand
        fields = ["brand_name", "name"]

# {"name" : Brand.name}

class CategorySerializer(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = ["id", "name", "parent"]



class ProductLineSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()

    class Meta():
        model = ProductLine
        exclude = ["id"]



class ProductSerializer(serializers.ModelSerializer):
    
    # Brand = BrandSerializer()
    # Category = CategorySerializer()
    brand_name = serializers.CharField(source="Brand.name")
    category_name = serializers.CharField(source="Category.name")

    product_line = ProductLineSerializer(many=True)

    class Meta():
        model = Product
        fields = [
            "brand_name",
            "category_name",
            "product_line",
            "name",
            "descriptions",
            "is_digital"
        ]
