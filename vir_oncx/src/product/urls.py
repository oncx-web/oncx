# product/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Example view for listing products
    path('<int:id>/', views.product_detail, name='product_detail'),  # Example view for product details
]
