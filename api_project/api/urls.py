from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BookListAPIView # Import both views

# Create a router instance
router = DefaultRouter()
# Register the BookViewSet with the router
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Route for the BookListAPIView
    path('books/', BookListAPIView.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet
    path('', include(router.urls)),
]