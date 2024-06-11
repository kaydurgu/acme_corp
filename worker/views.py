from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Profile
from .serializers import WorkerSerializer
class WorkersListView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = [permissions.IsAuthenticated,]  #admin custom field will be added]

class WorkersDetailView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class =WorkerSerializer
    permission_classes = [permissions.IsAuthenticated,]
