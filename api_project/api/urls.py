from django.urls import path
from .views import BookListCreateAPIView
from django.urls import include, path

urlpatterns = [
    path("api/books/", BookListCreateAPIView.as_view(), name="book_list_create"),
    path("api/", include("api.urls")),
]
