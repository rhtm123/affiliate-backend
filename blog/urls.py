
from django.urls import path

from blog import views
urlpatterns = [
    path('blogs/', views.BlogListCreate.as_view()),
    path('blog/<int:pk>/', views.BlogGetUpdate.as_view()),
    path('blog/<str:slug>/', views.BlogGetUpdateSlug.as_view()),
    path('blog/delete/<int:pk>/', views.BlogDelete.as_view()),
    path('blogs/blogproducts', views.BlogProductListCreate.as_view()),
    path('blog/blogs/<int:pk>/', views.BlogProductGetUpdate.as_view()),
    path('blog/blogs/delete/<int:pk>/', views.BlogProductDelete.as_view()),

    ## delete wala likhna hai..
]