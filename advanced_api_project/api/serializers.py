# api/serializers.py
from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    A serializer for the Book model.
    It serializes all fields and includes a custom validation to ensure the
    publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation to ensure the publication year is not in the future.
        """
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

class AuthorSerializer(serializers.ModelSerializer):
    """
    A serializer for the Author model.
    This serializer includes a nested representation of the related books,
    demonstrating how to handle a one-to-many relationship using a nested serializer.
    The 'books' field is the related_name we defined in the Book model's author foreign key.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        read_only_fields = ['books']