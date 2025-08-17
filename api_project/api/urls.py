from django.urls import path
from .views import BookListCreateAPIView
from django.urls import include, path
from .views import BookListAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('books/', BookListAPIView.as_view(), name='book-list'),
    path('', include(router.urls)),
]