from django.contrib import admin

# Register your models here.

from .models import PriceTrack, ProductVariantFeature, ProductVariantAffiliate, Product, ProductVariant, FeatureCategory, Feature

admin.site.register(FeatureCategory)

from django.core import serializers
from django.http import HttpResponse

def export_as_json(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/json")
    serializers.serialize("json", queryset, stream=response)
    return response

admin.site.add_action(export_as_json)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ("name", "value", "value_number")
    list_filter = ()
    search_fields = ("name", )

admin.site.register(Feature, FeatureAdmin)


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

class ProductAdmin(admin.ModelAdmin):

    inlines = [ProductVariantInline,]
    list_display = ('name','id','company', 'slug',"release_date","category")
    list_filter = ('company', 'category',)
    search_fields = ("name",)

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
    inlines = [ProductVariantAffiliateInline, ProductVariantFeatureInline]
    list_display = ('name','id','slug','product')
    list_filter = ('product',)
    search_fields = ('product__name', )

admin.site.register(ProductVariant, ProductVariantAdmin);

class ProductVariantFeatureAdmin(admin.ModelAdmin):
    list_per_page = 20  # Adjust this number as needed

    list_display = ("product_variant", 'feature')

    raw_id_fields = ['product_variant', "feature"]

    # list_filter = ("product_variant",)
    # # search_fields = ("product_variant__product__name", )

admin.site.register(ProductVariantFeature, ProductVariantFeatureAdmin);