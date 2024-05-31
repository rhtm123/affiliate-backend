from django.urls import path

from product import views
urlpatterns = [
    path('products/', views.ProductListCreate.as_view()),
    path('product/<int:pk>/', views.ProductGetUpdate.as_view()),
    path('product/<str:slug>/', views.ProductGetUpdateSlug.as_view()),
    path('product/delete/<int:pk>/', views.ProductDelete.as_view()),
    path('featurecategorys/', views.FeatureCategoryListCreate.as_view()),
    path('featurecategory/<int:pk>/', views.FeatureCategoryGetUpdate.as_view()),
    path('featurecategory/<str:slug>/', views.FeatureCategoryGetUpdateSlug.as_view()),
    path('featurecategory/delete/<int:pk>/', views.FeatureCategoryDelete.as_view()),
    path('features/', views.FeatureListCreate.as_view()),
    path('feature/<int:pk>/', views.FeatureGetUpdate.as_view()),
    path('feature/<str:slug>/', views.FeatureGetUpdateSlug.as_view()),
    path('feature/delete/<int:pk>/', views.FeatureDelete.as_view()),
    path('productvariants/', views.ProductVariantListCreate.as_view()),
    path('productvariant/<int:pk>/', views.ProductVariantGetUpdate.as_view()),
    path('productvariant/<str:slug>/', views.ProductVariantGetUpdateSlug.as_view()),
    path('productvariant/delete/<int:pk>/', views.ProductVariantDelete.as_view()),
    path('productvariantfeatures/', views.ProductVariantFeatureListCreate.as_view()),
    path('productvariantfeature/<int:pk>/', views.ProductVariantFeatureGetUpdate.as_view()),
    path('productvariantfeature/<str:slug>/', views.ProductVariantFeatureGetUpdateSlug.as_view()),
    path('productvariantfeature/delete/<int:pk>/', views.ProductVariantFeatureDelete.as_view()),
    path('productvariantaffiliates/', views.ProductVariantAffiliateListCreate.as_view()),
    path('productvariantaffiliate/<int:pk>/', views.ProductVariantAffiliateGetUpdate.as_view()),
    path('productvariantaffiliate/<str:slug>/', views.ProductVariantAffiliateGetUpdateSlug.as_view()),
    path('productvariantaffiliate/delete/<int:pk>/', views.ProductVariantAffiliateDelete.as_view()),
    path('pricetracks/', views.PriceTrackListCreate.as_view()),
    path('pricetrack/<int:pk>/', views.PriceTrackGetUpdate.as_view()),
    path('pricetrack/<str:slug>/', views.PriceTrackGetUpdateSlug.as_view()),
    path('pricetrack/delete/<int:pk>/', views.PriceTrackDelete.as_view()),
    ## delete wala likhna hai..
]