from django.contrib import admin
from .models import Product,Category,Brand,ProductImages

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductImages)
# Register your models here.
