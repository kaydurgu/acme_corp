from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
import django_filters
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
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description', 'category']
    ordering_fields = ['price']
    ordering = ['-price']
class ProductDetailView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated,]  #Admin group custom permissioon class will be added

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated and IsAdminWorker]

class ProductCategoryListView(APIView):
    def get(self, request):
        categories = Product.CATEGORY_CHOICES
        return Response(categories)
