from django.contrib import admin
from .models import Product

class ProductsAdmin(admin.ModelAdmin):
    fields = ['product_name','thumbnail','price']


admin.site.register(Product,ProductsAdmin)
