# product/views.py

from django.shortcuts import render, get_object_or_404
from .models import Product

def productlist(request):
    productlist = Product.objects.all()
   
    template='Product/product_list.html'
    context={'product_list':productlist}
    return render(request, template, context)


    

def productdetail(request, product_slug):
    print(product_slug)
    productdetail= Product.objects.get(slug=product_slug)
    template ='Product/product_detail.html'
    context ={'product_detail':productdetail}
    return render(request,template,context)


