# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters  # This import is required
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter  # Assuming you have created this file

class BookListView(generics.ListAPIView):
    """
    A generic view for retrieving a list of all books with filtering, searching,
    and ordering capabilities.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # Define the filter backends to use for this view
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Specify the custom filter set to use
    filterset_class = BookFilter

    # Specify the fields that can be searched on
    search_fields = ['title', 'author__name']

    # Specify the fields that can be used for ordering
    ordering_fields = ['title', 'publication_year', 'author__name']

class BookDetailView(generics.RetrieveAPIView):
    """
    A generic view for retrieving a single book by its ID.
    - Handles GET requests.
    - Permissions: Read-only access for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    A generic view for creating a new book.
    - Handles POST requests.
    - Permissions: Only authenticated users can create a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateView(generics.UpdateAPIView):
    """
    A generic view for updating an existing book.
    - Handles PUT/PATCH requests.
    - Permissions: Only authenticated users can update a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    A generic view for deleting a book.
    - Handles DELETE requests.
    - Permissions: Only authenticated users can delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
