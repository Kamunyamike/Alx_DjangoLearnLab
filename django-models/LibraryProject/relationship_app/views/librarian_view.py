from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Test function to check if the user is a Librarian
def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian, login_url='/no-access/', redirect_field_name=None)

