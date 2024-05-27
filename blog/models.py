from django.db import models
from django.conf import settings
from tag.models import Tag
from django.template.defaultfilters import slugify

from imagekit.models import ProcessedImageField # type: ignore
from imagekit.processors import ResizeToFill # type: ignore

from product.models import Product
from category.models import Category

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    seo_title = models.TextField(null=True, blank=True, max_length=100)
    seo_description = models.TextField(null=True, blank=True, max_length=255)
    detail = models.TextField()
    slug = models.SlugField(max_length=255,null=True, blank=True)
    is_published = models.BooleanField(default=False)

    img = ProcessedImageField(upload_to='blog/', processors=[ResizeToFill(1280, 720)], format='JPEG',options={'quality': 60 }, null=True,  blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    
    views = models.IntegerField(default=0)
    read_time = models.IntegerField(default=0) # in minutes
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


    def __str__(self):
        return self.title

class BlogProduct(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ranking = models.IntegerField(default=1)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)