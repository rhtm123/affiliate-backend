from django.urls import path

from product import views
urlpatterns = [
    path('products/', views.ProductListCreate.as_view()),
    path('product/<int:pk>/', views.ProductGetUpdate.as_view()),
    path('product/<str:slug>/', views.ProductGetUpdateSlug.as_view()),
    path('product/delete/<int:pk>/', views.ProductDelete.as_view()),
    ## delete wala likhna hai..
]