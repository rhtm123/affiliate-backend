from django.shortcuts import render

from .models import Product
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class MyPagination(PageNumberPagination):
	page_size = 15
	

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