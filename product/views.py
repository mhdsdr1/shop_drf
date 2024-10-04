from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Brand, Category, Product
from .serializer import BrandSerializer, CategorySerializer, ProductSerializer
from drf_spectacular.utils import extend_schema

class BrandsView(viewsets.ViewSet):
    queryset = Brand.objects.all()

    @extend_schema(responses = BrandSerializer)
    def list(self, request):

        print("object type:", self.queryset)

        serializer_data = BrandSerializer(self.queryset, many=True)

        print("seializer data:", serializer_data)
        print("data:", serializer_data.data)

        return Response(serializer_data.data)
    

class CategoryView(viewsets.ViewSet):
    queryset = Category.objects.all()

    @extend_schema(responses = CategorySerializer)
    def list(self, request):
        serializer_data = CategorySerializer(self.queryset, many=True)
        return Response(serializer_data.data)
    
        
class ProductView(viewsets.ViewSet):
    # queryset = Product.objects.all()
    # queryset = Product.objects.isactive()
    def get_queryset(self):
        return Product.objects.isactive()


    @extend_schema(responses = ProductSerializer)
    def list(self, request):
        serializer_data = ProductSerializer(self.get_queryset(), many=True)
        return Response(serializer_data.data)
    
    @action(methods=["get"], detail=False, url_path="category/(?P<category>.+)")
    def get_list_with_category_filter(self, request, category=None):
        serializer_data = ProductSerializer(self.get_queryset().filter(Category__name=category), many=True)
        return Response(serializer_data.data)

    def retrieve(self, request, pk=None):
        # serializer_data = ProductSerializer(self.queryset.filter(pk=pk), many=True)
        # serializer_data = ProductSerializer(self.queryset.filter(pk=pk).first())
        # serializer_data = ProductSerializer(self.queryset.get(pk=pk))
        serializer_data = ProductSerializer(get_object_or_404(self.get_queryset(), pk=pk))
        return Response(serializer_data.data)
        