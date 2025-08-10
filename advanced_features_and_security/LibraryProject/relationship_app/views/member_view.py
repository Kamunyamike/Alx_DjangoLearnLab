from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Test function to check if the user is a Member
def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_member, login_url='/no-access/', redirect_field_name=None)
def member_view(request):
    return render(request, 'member_view.html')