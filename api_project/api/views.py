from django.shortcuts import render
from rest_framework import generics
from .models import MyModel
from .serializers import MyModelSerializer
from .serializers import BookSerializer
from rest_framework import viewsets
from .models import MyModel
from .serializers import MyModelSerializer
from rest_framework import generics

# Create your views here.

class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
