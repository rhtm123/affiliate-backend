from django.contrib import admin

# Register your models here.


from blog.models import Blog 
from django_summernote.admin import SummernoteModelAdmin


class BlogAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('detail',)

admin.site.register(Blog, BlogAdmin)