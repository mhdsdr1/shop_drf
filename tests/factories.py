import factory
from product.models import Category, Brand, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        
    name = factory.Sequence(lambda x:f"categoty_{x}")

class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    # name = "brand_test"
    name = "brand_test"

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = "product_test"
    descriptions = "description_test"
    is_digital = False

    Brand = factory.SubFactory(BrandFactory)
    Category = factory.SubFactory(CategoryFactory)