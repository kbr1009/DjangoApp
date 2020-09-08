from django.contrib import admin
from .models import Product
# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    fields = ['product_name','price']


admin.site.register(Product,ProductsAdmin)
