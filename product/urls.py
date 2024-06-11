from django.urls import path, include

from .views import ProductListView, ProductDetailView, ProductCreateView, ProductCategoryListView

urlpatterns = [
    path('',ProductListView.as_view(),name='product-list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('create/', ProductCreateView.as_view(),name='product-detail'),
    path('cat/', ProductCategoryListView.as_view(), name='product-all-cats'),
]
