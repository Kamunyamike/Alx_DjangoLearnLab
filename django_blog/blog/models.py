from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    # Foreign key linking to the Post model, establishing a many-to-one relationship.
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    # Foreign key to Django’s User model, indicating the user who wrote the comment.
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # TextField for the comment's text.
    content = models.TextField()
    # DateTimeField that records the time the comment was made.
    created_at = models.DateTimeField(default=datetime.now)
    # DateTimeField that records the last time the comment was updated.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'
    
    class Meta:
        ordering = ['-created_at']
        