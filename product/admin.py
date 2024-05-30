from django.contrib import admin

# Register your models here.

from .models import PriceTrack, ProductVariantFeature, ProductVariantAffiliate, Product, ProductVariant, FeatureCategory, Feature

admin.site.register(FeatureCategory)
admin.site.register(Feature)

class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

class ProductAdmin(admin.ModelAdmin):

    inlines = [ProductVariantInline,]
    # list_display = ('name','get_course_name')
    list_filter = ('company', 'category',)

admin.site.register(Product, ProductAdmin);



class ProductVariantFeatureInline(admin.TabularInline):
    model = ProductVariantFeature
    extra = 1 

class ProductVariantAffiliateInline(admin.TabularInline):
    model = ProductVariantAffiliate
    extra = 1

class PriceTrackInline(admin.TabularInline):
    model = PriceTrack
    extra = 1


class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductVariantFeatureInline,ProductVariantAffiliateInline, PriceTrackInline]
    # list_display = ('name','get_course_name')
    list_filter = ('product',)

admin.site.register(ProductVariant, ProductVariantAdmin);
