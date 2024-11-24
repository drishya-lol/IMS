from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from .models import Product, ProductCategory, Department, Vendor, Purchase, Sell
from .serializers import ProductSerializer, ProductCategorySerializer, DepartmentSerializer, VendorSerializer, PurchaseSerializer, SellSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view #fuctions based api view
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    
class ProductTypeApiView(GenericAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAuthenticated]
    
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
    permission_classes = [IsAuthenticated]
    
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
    
class PurchaseApiView(GenericAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:  # Retrieve a specific purchase
            purchaseObj = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.get_serializer(purchaseObj)
            return Response(serializer.data)
        else:  # Retrieve all purchases
            purchaseObjects = self.get_queryset()
            serializer = self.get_serializer(purchaseObjects, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        purchaseObj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(purchaseObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        purchaseObj = get_object_or_404(self.get_queryset(), pk=pk)
        purchaseObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SellApiView(GenericAPIView):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    permission_classes = [IsAuthenticated]  

    def get(self, request, pk=None):
        if pk:  # Retrieve a specific sell record
            sellObj = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.get_serializer(sellObj)
            return Response(serializer.data)
        else:  # Retrieve all sell records
            sellObjects = self.get_queryset()
            serializer = self.get_serializer(sellObjects, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        sellObj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(sellObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sellObj = get_object_or_404(self.get_queryset(), pk=pk)
        sellObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentApiView(GenericAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:  # Retrieve a specific department
            departmentObj = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.get_serializer(departmentObj)
            return Response(serializer.data)
        else:  # Retrieve all departments
            departmentObjects = self.get_queryset()
            serializer = self.get_serializer(departmentObjects, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        departmentObj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(departmentObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        departmentObj = get_object_or_404(self.get_queryset(), pk=pk)
        departmentObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VendorApiView(GenericAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk:  # Retrieve a specific vendor
            vendorObj = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.get_serializer(vendorObj)
            return Response(serializer.data)
        else:  # Retrieve all vendors
            vendorObjects = self.get_queryset()
            serializer = self.get_serializer(vendorObjects, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        vendorObj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(vendorObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        vendorObj = get_object_or_404(self.get_queryset(), pk=pk)
        vendorObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST']) #which requests are allowed
def register(request):
    password = request.data.get('password')
    hash_password = make_password(password)
    data = request.data.copy()
    data['password'] = hash_password
    serializer = UserSerializer(data = data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)

@api_view(['POST']) #which requests are allowed
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user == None:
        return Response("Invalid Credentials", status = status.HTTP_400_BAD_REQUEST)
    else:
        token,_ = Token.objects.get_or_create(user=user)
        return Response(token.key, status = status.HTTP_200_OK)