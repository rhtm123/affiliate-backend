from .models import Product
from .models import FeatureCategory
from .models import Feature
from .models import ProductVariant
from .models import ProductVariantFeature
from .models import ProductVariantAffiliate
from .models import PriceTrack
from rest_framework import serializers


class ProductVariantFeatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductVariantFeature
        fields = '__all__'

        depth = 1

class ProductVariantAffiliateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductVariantAffiliate
        fields = '__all__'
        
class ProductVariantSerializer(serializers.ModelSerializer):
    affiliates = ProductVariantAffiliateSerializer(many=True, read_only=True, source='productvariantaffiliate_set')  # Nested serializer for children
    # features = ProductVariantFeatureSerializer(many=True, read_only=True, source="productvariantfeature_set")
    
    class Meta:
        model = ProductVariant
        fields = ['id','name','product', "slug", "affiliates"]    


# class ProductVariant2Serializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = ProductVariant
#         fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True, source='productvariant_set')
    
    class Meta:
        model = Product
        fields = ['name', 'company', 'release_date', 'detail', 'category', 'variants']
        depth = 1

class FeatureCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FeatureCategory
        fields = '__all__'


class ProductVariantAffiliateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductVariantAffiliate
        fields = '__all__'
        
class ProductVariantSerializer(serializers.ModelSerializer):
    affiliates = ProductVariantAffiliateSerializer(many=True, read_only=True, source='productvariantaffiliate_set')  # Nested serializer for children
    
    class Meta:
        model = ProductVariant
        fields = ['id','name','product', "slug", "affiliates"]
        depth = 2



        
class FeatureSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feature
        fields = '__all__'
        
 
        

        

class PriceTrackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PriceTrack
        fields = '__all__'
        