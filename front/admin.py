from django.contrib import admin
from .models import Product

class ProductsAdmin(admin.ModelAdmin):
    fields = ['product_name','price','thumbnail','description']


admin.site.register(Product,ProductsAdmin)
