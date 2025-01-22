from django.shortcuts import render
from .models import Product, ProductCategory, Department, Vendor, Purchase, Sell
from .serializer import ProductSerializer, ProductCategorySerializer, DepartmentSerializer, UserSerializer, VendorSerializer, PurchaseSerializer, SellSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser, DjangoModelPermissions
from django.contrib.auth.models import Group
# Create your views here.
class ProductApiView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filterset_fields = ['category', 'department']
    search_fields = ['name', 'description']
    
class ProductCategoryApiView(GenericAPIView):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    
    def get(self, request):
        productTypeObjs = self.get_queryset()
        filter_data = self.filter_queryset(productTypeObjs)
        paginated_data = self.paginate_queryset(filter_data)
        serializer = self.get_serializer(paginated_data, many=True)
        response = self.get_paginated_response(serializer.data)
        return Response(response)
    
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
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    
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
    permission_classes = [IsAuthenticated]
    
class VendorApiView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes = [IsAuthenticated]
    
class PurchaseApiView(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
    
class SellApiView(ModelViewSet):
    queryset = Sell.objects.all()
    serializer_class = SellSerializer
    permission_classes = [IsAuthenticated]
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registerEmployee(request):
    if request.user.groups.name == 'Management':
        employeeGroup = Group.objects.get(name='Employee')
        password = request.data.get('password')
        hashed_password = make_password(password)
        data = request.data.copy()
        data['password'] = hashed_password
        data['groups'] = employeeGroup.id
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        return Response('Permission Denied', status=status.HTTP_403_FORBIDDEN)
                        
@api_view(['POST'])
@permission_classes([IsAdminUser])
def registerManagemenet(request):
    managementGroup = Group.objects.get(name='Management')
    password = request.data.get('password')
    hashed_password = make_password(password)
    data = request.data.copy()
    data['password'] = hashed_password
    data['groups'] = managementGroup.id
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
        token, _ = Token.objects.get_or_create(user=user)
        return Response(token.key)
    