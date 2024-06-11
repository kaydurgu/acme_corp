from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions
from product.models import Product

from .serializers import ProductSerializer

# Create your views here.
#custom permission
class IsAdminWorker(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.groups.filter(name='Admin').exists()

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]
class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,]  #Admin group custom permissioon class will be added
