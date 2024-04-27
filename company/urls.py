
from django.urls import path

from company import views
urlpatterns = [
    path('companys/', views.CompanyListCreate.as_view()),
    path('company/<int:pk>/', views.CompanyGetUpdate.as_view()),
    path('company/<str:slug>/', views.CompanyGetUpdateSlug.as_view()),
    path('company/delete/<int:pk>/', views.CompanyDelete.as_view()),

    ## delete wala likhna hai..
]