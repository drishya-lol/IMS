from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product, ProductCategory, Department, Vendor, Purchase, Sell
from .serializer import ProductSerializer, ProductCategorySerializer, DepartmentSerializer, UserSerializer, VendorSerializer, PurchaseSerializer, SellSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# Create your views here.
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class ProductCategoryApiView(GenericAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
    def get(self, request):
        productTypeObjs = self.get_queryset()
        serializer = self.get_serializer(productTypeObjs, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ProductCategoryIdApiView(GenericAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    
    def get(self, request, pk):
        productTypeObj = self.get_object()                  #ProductCategory.objects.get(pk=pk)
        serializer = self.get_serializer(productTypeObj)
        return Response(serializer.data)
    
    def put(self, request, pk):
        productTypeObj = self.get_object()
        serializer = self.get_serializer(productTypeObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        productCategoryObj = self.get_object()
        productCategoryObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class DepartmentApiView(ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class VendorApiView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    
class PurchaseApiView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    
class SellApiView(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    
@api_view(['POST'])
def register(request):
    password = request.data.get('password')
    hashed_password = make_password(password)
    data = request.data.copy()
    data['password'] = hashed_password
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user == None:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        Token.objects.create(user=user)
    