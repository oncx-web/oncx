# product/urls.py

from django.urls import path
from . import views

app_name ='product'

urlpatterns = [
    path('', views.productlist, name='product_list'),  # Example view for listing products
    path('<slug:product_slug>/', views.productdetail, name='product_detail'),  # Example view for product details
]
