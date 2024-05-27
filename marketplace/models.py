from django.db import models

from django.template.defaultfilters import slugify


# Create your models here.
from django.db import models

class MarketPlace(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255,null=True, blank=True)

    detail = models.TextField()
    website = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(MarketPlace, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
