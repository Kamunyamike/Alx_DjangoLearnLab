from django.urls import path
from .views import BookListCreateAPIView
from django.urls import include, path

urlpatterns = [
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path("api/", include("api.urls")),
]
