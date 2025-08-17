# api/test_views.py
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints to ensure they behave as expected.
    """
    def setUp(self):
        """
        Set up the testing environment before each test.
        - Create a test client for making API requests.
        - Create a test user for authentication.
        - Create an author and book instance for testing.
        """
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='George Orwell')
        self.book = Book.objects.create(
            title='1984',
            publication_year=1949,
            author=self.author
        )

        # Define API endpoint URLs for easier testing
        self.list_url = reverse('book-list')
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    def test_list_books(self):
        """
        Test that the book list view returns a list of books and a 200 OK status.
        """
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_create_book_authenticated(self):
        """
        Test that an authenticated user can create a new book.
        """
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author.pk
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        """
        Test that an unauthenticated user cannot create a new book.
        """
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author.pk
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 1)

    def test_retrieve_book(self):
        """
        Test that a single book can be retrieved by its primary key.
        """
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], '1984')

    def test_update_book_authenticated(self):
        """
        Test that an authenticated user can update an existing book.
        """
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Nineteen Eighty-Four'}
        response = self.client.patch(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Nineteen Eighty-Four')

    def test_update_book_unauthenticated(self):
        """
        Test that an unauthenticated user cannot update a book.
        """
        data = {'title': 'Nineteen Eighty-Four'}
        response = self.client.patch(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, '1984')

    def test_delete_book_authenticated(self):
        """
        Test that an authenticated user can delete a book.
        """
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        """
        Test that an unauthenticated user cannot delete a book.
        """
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_by_title(self):
        """
        Test filtering books by title.
        """
        Book.objects.create(title='The Great Gatsby', publication_year=1925, author=self.author)
        response = self.client.get(f'{self.list_url}?title=1984')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_search_by_author_name(self):
        """
        Test searching books by author name.
        """
        Book.objects.create(title='The Great Gatsby', publication_year=1925, author=self.author)
        response = self.client.get(f'{self.list_url}?search=George')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], '1984')

    def test_order_by_publication_year_desc(self):
        """
        Test ordering books by publication year in descending order.
        """
        Book.objects.create(title='Animal Farm', publication_year=1945, author=self.author)
        response = self.client.get(f'{self.list_url}?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1949)
        self.assertEqual(response.data[1]['publication_year'], 1945)
