from django.shortcuts import render

from blog.models import Blog,BlogProduct
from blog.serializers import BlogSerializer,BlogProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class MyPagination(PageNumberPagination):
	page_size = 15
	

class BlogListCreate(generics.ListCreateAPIView):
	queryset = Blog.objects.all().order_by('id')
	serializer_class = BlogSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
	filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
	filterset_fields = ('author', 'is_published', 'tags', 'category', )
	search_fields = ('title',)
	ordering_fields = ('views','likes',"created","updated")
	pagination_class = MyPagination


class BlogGetUpdate(generics.RetrieveUpdateAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	permission_classes = (AllowAny,)

class BlogGetUpdateSlug(generics.RetrieveUpdateAPIView):
	lookup_field = "slug"
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	permission_classes = (AllowAny,)
	
class BlogDelete(generics.DestroyAPIView):
	queryset = Blog.objects.all()
	serializer_class = BlogSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
 
class BlogProductListCreate(generics.ListCreateAPIView):
    queryset = BlogProduct.objects.all().order_by('id')
    serializer_class = BlogProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
    filterset_fields = ('blog', 'product')
    search_fields = ('name',)
    ordering_fields = ("created","updated")
    pagination_class = MyPagination
    
class BlogProductGetUpdate(generics.RetrieveUpdateAPIView):
	queryset = BlogProduct.objects.all()
	serializer_class = BlogProductSerializer
	permission_classes = (AllowAny,)
	
class BlogProductDelete(generics.DestroyAPIView):
	queryset = BlogProduct.objects.all()
	serializer_class = BlogProductSerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)