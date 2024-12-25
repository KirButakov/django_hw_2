from django.urls import path
from . import views

urlpatterns = [
    path('product/create/', views.product_create, name='product_create'),
    path('product/update/<int:pk>/', views.product_update, name='product_update'),
    path('product/delete/<int:pk>/', views.product_delete, name='product_delete'),
    path('products/', views.product_list, name='product_list'),
]
