from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Profile
from product.models import Product
from product.serializers import ProductSerializer
from .serializers import WorkerSerializer, WorkerUpdateSerializer

class IsAdminWorker(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.groups.filter(name='Admin').exists()

class WorkersListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [permissions.IsAuthenticated and IsAdminWorker]  #admin custom field will be added]

class WorkersDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class =WorkerSerializer
    permission_classes = [permissions.IsAuthenticated,]
class WorkerUpdateView(RetrieveUpdateDestroyAPIView ):
    queryset = Profile.objects.all()
    serializer_class = WorkerUpdateSerializer
    permission_classes = [permissions.IsAuthenticated and IsAdminWorker]
class WorkerResponsibleListView(ListAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.filter(responsible_worker=self.kwargs['pk'])