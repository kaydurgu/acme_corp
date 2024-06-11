from django.urls import path, include

from .views import ProductListView, ProductDetailView, ProductCreateView, ProductCategoryListView, ProductUpdateView

urlpatterns = [
    path('',ProductListView.as_view(),name='product-list'),
    path('<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('create/', ProductCreateView.as_view(),name='product-create'),
    path('cat/', ProductCategoryListView.as_view(), name='product-all-cats'),
]
