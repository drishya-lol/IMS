"""
URL configuration for ims project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import ProductApiView, ProductTypeApiView, ProductTypeIdApiView, PurchaseApiView, SellApiView, DepartmentApiView, VendorApiView, register, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', ProductApiView.as_view({'get':'list', 'post':'create'})),
    path('product/<int:pk>/', ProductApiView.as_view({'get': 'retrieve', 'put': 'update', 'patch':'partial_update', 'delete': 'destroy'})),
    path('productcategory/', ProductTypeApiView.as_view()),
    path('productcategory/<int:pk>', ProductTypeIdApiView.as_view()),
    path('purchases/', PurchaseApiView.as_view(), name='purchase-list'),
    path('purchases/<int:pk>/', PurchaseApiView.as_view(), name='purchase-detail'),
    path('sells/', SellApiView.as_view(), name='sell-list'),
    path('sells/<int:pk>/', SellApiView.as_view(), name='sell-detail'),
    path('departments/', DepartmentApiView.as_view(), name='department-list'),
    path('departments/<int:pk>/', DepartmentApiView.as_view(), name='department-detail'),
    path('vendors/', VendorApiView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorApiView.as_view(), name='vendor-detail'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
