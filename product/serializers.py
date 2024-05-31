from .models import Product
from .models import FeatureCategory
from .models import Feature
from .models import ProductVariant
from .models import ProductVariantFeature
from .models import ProductVariantAffiliate
from .models import PriceTrack
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'

class FeatureCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FeatureCategory
        fields = '__all__'
        
class FeatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feature
        fields = '__all__'
        
class ProductVariantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductVariant
        fields = '__all__'       
        
class ProductVariantFeatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductVariantFeature
        fields = ['product_variant','feature']
        depth = 1
        
class ProductVariantAffiliateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductVariantAffiliate
        fields = '__all__'
        
class PriceTrackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PriceTrack
        fields = '__all__'
        