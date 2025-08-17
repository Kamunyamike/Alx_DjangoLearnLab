# api/urls.py
from django.urls import path
from .views import BookListCreateView, BookDetailView

urlpatterns = [
    # URL pattern for listing all books and creating a new one
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    # URL pattern for retrieving, updating, or deleting a single book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
]