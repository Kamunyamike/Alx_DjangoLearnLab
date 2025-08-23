# accounts/urls.py
from django.urls import path
from .views import (
    UserRegistrationView, UserLoginView, UserProfileView,
    FollowUserView, UnfollowUserView # Import the new views
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('follow/<int:pk>/', FollowUserView.as_view(), name='follow'),
    path('unfollow/<int:pk>/', UnfollowUserView.as_view(), name='unfollow'),
]