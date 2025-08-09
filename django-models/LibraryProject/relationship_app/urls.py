from django.urls import path
from . import views
from .views import LibraryDetailView, book_list
from .views import list_books

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', views.book_list, name='home'),  # Redirect to book list on home page

]
