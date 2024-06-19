from django.shortcuts import render

from .models import Product
from .models import FeatureCategory
from .models import Feature
from .models import ProductVariant
from .models import ProductVariantFeature
from .models import ProductVariantAffiliate
from .models import PriceTrack
from .serializers import ProductSerializer
from .serializers import FeatureCategorySerializer
from .serializers import FeatureSerializer
from .serializers import ProductVariantSerializer
from .serializers import ProductVariantFeatureSerializer
from .serializers import ProductVariantAffiliateSerializer
from .serializers import PriceTrackSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class MyPagination(PageNumberPagination):
    page_size = 15


class FeaturePagination(PageNumberPagination):
    page_size = 100
    

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filterset_fields = ('company', 'category')
    search_fields = ('name',)
    ordering_fields = ("created","updated")
    pagination_class = MyPagination


class ProductGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)

class ProductGetUpdateSlug(generics.RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    
class ProductDelete(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
 
class FeatureCategoryListCreate(generics.ListCreateAPIView):
    queryset = FeatureCategory.objects.all().order_by('id')
    serializer_class = FeatureCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    # filterset_fields = ('feature',)
    search_fields = ('name',)
    ordering_fields = ("created","updated")
    pagination_class = MyPagination

class FeatureCategoryGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = FeatureCategory.objects.all()
    serializer_class = FeatureCategorySerializer
    permission_classes = (AllowAny,)

class FeatureCategoryGetUpdateSlug(generics.RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = FeatureCategory.objects.all()
    serializer_class = FeatureCategorySerializer
    permission_classes = (AllowAny,)
    
class FeatureCategoryDelete(generics.DestroyAPIView):
    queryset = FeatureCategory.objects.all()
    serializer_class = FeatureCategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
 
class FeatureListCreate(generics.ListCreateAPIView):
    queryset = Feature.objects.all().order_by('id')
    serializer_class = FeatureSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filterset_fields = ('feature_category',)
    search_fields = ('name',)
    ordering_fields = ("created","updated")
    pagination_class = FeaturePagination

class FeatureGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (AllowAny,)

class FeatureGetUpdateSlug(generics.RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (AllowAny,)
    
class FeatureDelete(generics.DestroyAPIView):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
 
class ProductVariantListCreate(generics.ListCreateAPIView):
    queryset = ProductVariant.objects.all().order_by('id')
    serializer_class = ProductVariantSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filterset_fields = ('product',)
    search_fields = ('name',)
    ordering_fields = ("created","updated")
    pagination_class = MyPagination

class ProductVariantGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = (AllowAny,)

class ProductVariantGetUpdateSlug(generics.RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = (AllowAny,)
    
class ProductVariantDelete(generics.DestroyAPIView):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ProductVariantFeatureListCreate(generics.ListCreateAPIView):
    queryset = ProductVariantFeature.objects.all().order_by('id')
    serializer_class = ProductVariantFeatureSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filterset_fields = ('product_variant','feature')
    # search_fields = ('name',)
    ordering_fields = ("created","updated")
    pagination_class = FeaturePagination


class ProductVariantFeatureGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = ProductVariantFeature.objects.all()
    serializer_class = ProductVariantFeatureSerializer
    permission_classes = (AllowAny,)

class ProductVariantFeatureGetUpdateSlug(generics.RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = ProductVariantFeature.objects.all()
    serializer_class = ProductVariantFeatureSerializer
    permission_classes = (AllowAny,)
    
class ProductVariantFeatureDelete(generics.DestroyAPIView):
    queryset = ProductVariantFeature.objects.all()
    serializer_class = ProductVariantFeatureSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ProductVariantAffiliateListCreate(generics.ListCreateAPIView):
    queryset = ProductVariantAffiliate.objects.all().order_by('id')
    serializer_class = ProductVariantAffiliateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filterset_fields = ('product_variant','marketplace',)
    # search_fields = ('name',)
    ordering_fields = ("created","updated")
    pagination_class = MyPagination

class ProductVariantAffiliateGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = ProductVariantAffiliate.objects.all()
    serializer_class = ProductVariantAffiliateSerializer
    permission_classes = (AllowAny,)

class ProductVariantAffiliateGetUpdateSlug(generics.RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = ProductVariantAffiliate.objects.all()
    serializer_class = ProductVariantAffiliateSerializer
    permission_classes = (AllowAny,)
    
class ProductVariantAffiliateDelete(generics.DestroyAPIView):
    queryset = ProductVariantAffiliate.objects.all()
    serializer_class = ProductVariantAffiliateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class PriceTrackListCreate(generics.ListCreateAPIView):
    queryset = PriceTrack.objects.all().order_by('id')
    serializer_class = PriceTrackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filterset_fields = ('affiliate',)
    # search_fields = ('name',)
    ordering_fields = ("created","updated")
    pagination_class = MyPagination

class PriceTrackGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = PriceTrack.objects.all()
    serializer_class = PriceTrackSerializer
    permission_classes = (AllowAny,)

class PriceTrackGetUpdateSlug(generics.RetrieveUpdateAPIView):
    lookup_field = "slug"
    queryset = PriceTrack.objects.all()
    serializer_class = PriceTrackSerializer
    permission_classes = (AllowAny,)
    
class PriceTrackDelete(generics.DestroyAPIView):
    queryset = PriceTrack.objects.all()
    serializer_class = PriceTrackSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)