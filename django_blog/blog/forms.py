# blog/forms.py
from django import forms
from .models import Comment, Post
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            # This is the correct way to use a custom widget
            # for the 'tags' field.
            'tags': TagWidget(attrs={'class': 'tag-input-field', 'placeholder': 'Tags separated by commas'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }