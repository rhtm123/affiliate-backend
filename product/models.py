# models.py
from django.db import models
from category.models import Category
from company.models import Company

class Product(models.Model):
    name = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    detail = models.TextField()
    mrp = models.DecimalField(max_digits=10, decimal_places=2) # MRP 
    category = models.ForeignKey(Category , on_delete=models.CASCADE)

    amazonAffiliate = models.TextField(null=True, blank=True)
    flipkartAffiliate = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class PriceTrack(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2) # MRP 

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)