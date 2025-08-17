# api/urls.py
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    # URLs for the separate CRUD views
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
]