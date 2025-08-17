# api/filters.py
import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    """
    A custom filter set for the Book model.
    This class specifies the fields that can be used to filter a queryset.
    """
    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'author__name': ['exact', 'icontains'],
            'publication_year': ['exact', 'gte', 'lte'],
        }

    order_by = django_filters.OrderingFilter(
        fields=(
            ('title', 'title'),
            ('publication_year', 'publication_year'),
            ('author__name', 'author__name'),
        ),
        field_labels={
            'title': 'Title',
            'publication_year': 'Publication Year',
            'author__name': 'Author Name',
        }
    )