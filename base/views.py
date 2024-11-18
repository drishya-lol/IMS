from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import Product, ProductCategory, Department, Vendor, Purchase, Sell
from .serializers import ProductSerializer, ProductCategorySerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductTypeApiView(GenericAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
    def get(self, request):
        productCategoryObjects = self.get_queryset()
        serializer = self.get_serializer(productCategoryObjects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProductTypeIdApiView(GenericAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
    def get(self, request, pk):
        # ProductCategory.objects.get(id=pk)
        productCategoryObj = self.get_object() # this does the same thing as above
        serializer = self.get_serializer(productCategoryObj)
        return Response(serializer.data)
    
    def put(self, request, pk):
        ProductCategoryObj = self.get_object()
        serializer = self.get_serializer(ProductCategoryObj, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        ProductCategoryObj = self.get_object()
        ProductCategoryObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)