from django import forms
from .models import Book  # Replace with your actual model if different

class ExampleForm(forms.ModelForm):
    """
    Example form to demonstrate secure form handling.
    This form automatically includes CSRF protection in templates.
    """

    class Meta:
        model = Book
        fields = ['title', 'author']  # Include only safe fields

    # Optional: add extra validation for enhanced security
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid input detected.")
        return title
    
