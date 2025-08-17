from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer
# Create your views here.
class BookListCreateView(generics.ListCreateAPIView):
    """
    A generic view for listing all books and creating a new book.
    - Handles GET requests to list all books.
    - Handles POST requests to create a new book.
    - Uses IsAuthenticatedOrReadOnly permission, allowing anyone to view books,
      but only authenticated users can create new ones.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    A generic view for retrieving, updating, and deleting a single book.
    - Handles GET requests to retrieve a specific book by its primary key.
    - Handles PUT/PATCH requests to update a book.
    - Handles DELETE requests to delete a book.
    - Uses IsAuthenticatedOrReadOnly permission, allowing anyone to view a book,
      but only authenticated users can update or delete it.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
