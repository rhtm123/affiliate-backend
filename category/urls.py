# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('categorys/', views.CategoryListCreate.as_view()),
    path('category/<int:pk>/', views.CategoryGetUpdate.as_view()),
    path('category/<str:slug>/', views.CategoryGetUpdateSlug.as_view()),
    path('category/delete/<int:pk>/', views.CategoryDelete.as_view()),
]