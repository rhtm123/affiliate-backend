from django.contrib import admin

# Register your models here.
from django.forms import BaseInlineFormSet
from django.core.paginator import Paginator
from django.utils.functional import cached_property


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
    extra = 0


    fields = ['feature', 'is_key_feature']  # List only the necessary fields
    raw_id_fields = ['feature',]
    can_delete = False  # Optionally disable deletion if not needed


class ProductVariantAffiliateInline(admin.TabularInline):
    model = ProductVariantAffiliate
    extra = 1

class PriceTrackInline(admin.TabularInline):
    model = PriceTrack
    extra = 1

# class ProductVariantFeatureInline(admin.StackedInline):
#     model = ProductVariantFeature
#     extra = 0
#     # formset = LimitedInlineFormSet
    

class ProductVariantAdmin(admin.ModelAdmin):
    inlines = [ProductVariantAffiliateInline, ProductVariantFeatureInline]
    list_display = ('name','id','slug','product')
    list_filter = ('product',)
    search_fields = ('product__name', )

admin.site.register(ProductVariant, ProductVariantAdmin);

class ProductVariantFeatureAdmin(admin.ModelAdmin):
    list_per_page = 20  # Adjust this number as needed

    list_display = ("variant_name", "product_variant", 'feature')

    # raw_id_fields = ['product_variant', "feature"]

    # list_filter = ("product_variant",)

    def variant_name(self, obj):
        return obj.product_variant.product
    search_fields = ("product_variant__product__name", )

admin.site.register(ProductVariantFeature, ProductVariantFeatureAdmin);