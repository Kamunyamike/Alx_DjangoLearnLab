from django.urls import path
from . import views
from .views import LibraryDetailView, book_list
from .views import list_books
from .views import BookListView, register_view, login_view, logout_view

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', BookListView.as_view(), name='home'),  # Redirect to book list on home page
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]