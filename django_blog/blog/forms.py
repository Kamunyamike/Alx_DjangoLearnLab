# blog/forms.py
from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        # Use the 'widgets' dictionary to apply a custom widget to a field.
        widgets = {
            'tags': forms.TextInput(attrs={'class': 'tag-input-field', 'placeholder': 'Tags separated by commas'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
