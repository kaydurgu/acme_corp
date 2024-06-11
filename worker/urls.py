from django.urls import path, include
from .views import WorkersListView, WorkersDetailView, WorkerUpdateView,WorkerResponsibleListView
urlpatterns = [
    path('', WorkersListView.as_view(), name='workers-list'),
    path('<int:pk>/', WorkersDetailView.as_view(), name='workers-detail' ),
    path('auth/', include('rest_framework.urls')),
    path('<int:pk>/update',WorkerUpdateView.as_view(), name='workers-update-delete-view'),
    path('<int:pk>/responsible',WorkerResponsibleListView.as_view(), name='workers-responsible')
]
