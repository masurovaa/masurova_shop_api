from django.urls import path
from .views import (
    CategoryListCreateAPIView,
    CategoryDetailAPIView,
    ProductListCreateAPIView,
    ProductDetailAPIView,
    ProductWithReviewsAPIView,
    OwnerProductListAPIView,
)

urlpatterns = [
    path("", ProductListCreateAPIView.as_view()),
    path("<int:id>/", ProductDetailAPIView.as_view()),
    path("categories/", CategoryListCreateAPIView.as_view()),
    path("categories/<int:id>/", CategoryDetailAPIView.as_view()),
    path("reviews/", ProductWithReviewsAPIView.as_view()),
    path("my/", OwnerProductListAPIView.as_view()),
]
