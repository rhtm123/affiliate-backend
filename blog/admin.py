from django.contrib import admin

# Register your models here.


from blog.models import Blog, BlogProduct
from django_summernote.admin import SummernoteModelAdmin


class BlogProductTabular(admin.TabularInline):
    model = BlogProduct
    extra = 1
    raw_id_fields = ['product',]


class BlogAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('detail',)
    inlines = [BlogProductTabular]

admin.site.register(Blog, BlogAdmin)