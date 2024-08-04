# product/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.productlist, name='product_list'),  # Example view for listing products
    path('<int:id>/', views.productdetail, name='product_detail'),  # Example view for product details
]
