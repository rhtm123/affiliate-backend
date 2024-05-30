# models.py
from django.db import models
from category.models import Category
from company.models import Company
from marketplace.models import MarketPlace

class Product(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # model 
    # release_date
    # 
    detail = models.TextField()
    # mrp = models.DecimalField(max_digits=10, decimal_places=2) # MRP 
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    mrp = models.DecimalField(max_digits=10, decimal_places=2) # MRP 
    name = models.CharField(max_length=255, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)


    
class ProductAffiliate(models.Model):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, blank=True)
    marketplace = models.ForeignKey(MarketPlace, on_delete=models.CASCADE, blank=True, null=True)
    affiliate_link = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
class PriceTrack(models.Model):
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # MRP 

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)