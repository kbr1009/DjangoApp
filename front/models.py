from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=258)
