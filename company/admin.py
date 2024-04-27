from django.contrib import admin

# Register your models here.

from .models import Company

class CompanyAdmin(admin.ModelAdmin):
    pass 

    # list_display = ('name','get_course_name')
    # list_filter = ('program', 'course',)

admin.site.register(Company, CompanyAdmin);