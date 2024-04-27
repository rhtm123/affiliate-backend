from django.shortcuts import render

from .models import Company
from .serializers import CompanySerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class MyPagination(PageNumberPagination):
	page_size = 15
	

class CompanyListCreate(generics.ListCreateAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)
	filter_backends = (DjangoFilterBackend, filters.SearchFilter,filters.OrderingFilter)
	# filterset_fields = ('author', 'is_published', 'tags')
	search_fields = ('name',)
	ordering_fields = ("created","updated")
	pagination_class = MyPagination


class CompanyGetUpdate(generics.RetrieveUpdateAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	permission_classes = (AllowAny,)

class CompanyGetUpdateSlug(generics.RetrieveUpdateAPIView):
	lookup_field = "slug"
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	permission_classes = (AllowAny,)
	
class CompanyDelete(generics.DestroyAPIView):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	permission_classes = (IsAuthenticatedOrReadOnly,)