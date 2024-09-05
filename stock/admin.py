from django.contrib import admin
from .models import Stock, Product, ProductInStock

admin.site.register(Stock)
admin.site.register(Product)
admin.site.register(ProductInStock)
