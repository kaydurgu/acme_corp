from django.urls import path, include
from .views import WorkersListView, WorkersDetailView
urlpatterns = [
    path('', WorkersListView.as_view(), name='workers-list'),
    path('<int:pk>/', WorkersDetailView.as_view(), name='workers-detail' ),

]
