# api/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    A generic view for retrieving a list of all books.
    - Handles GET requests.
    - Permissions: Read-only access for all users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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
