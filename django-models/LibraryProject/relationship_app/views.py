from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book
from .models import Library  # Explicit separate import

# Function-based view for listing books
def book_list(request):
    books = Book.objects.all()  # Required query
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view for listing books
class BookListView(ListView):
    model = Book
    template_name = 'relationship_app/book_list.html'
    context_object_name = 'books'


# Class-based view for displaying a library’s details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context
