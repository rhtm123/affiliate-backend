from .models import Category
from category.serializers import CategorySerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class MyPagination(PageNumberPagination):
	page_size = 15

class CategoryListCreate(generics.ListCreateAPIView):
	queryset = Category.objects.all().order_by('id')
	serializer_class = CategorySerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
	filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
	# filterset_fields = ('author', 'is_published', 'tags')
	# search_fields = ('header', 'sub_header')
	pagination_class = MyPagination


class CategoryGetUpdate(generics.RetrieveUpdateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = (AllowAny,)

class CategoryGetUpdateSlug(generics.RetrieveUpdateAPIView):
	lookup_field = "slug"
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = (AllowAny,)
	
class CategoryDelete(generics.DestroyAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)