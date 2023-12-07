from django.shortcuts import render
from .models import Profile


def index(request):
    """
    View for the index page of profiles.

    This view retrieves all Profile objects from the database and passes them
    to the 'profiles/index.html' template.
    It is used to display a list of all user profiles available in the system.

    Args:
        request: The HttpRequest object.

    Returns:
        HttpResponse: The rendered index page with the list of profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


def profile(request, username):
    """
    View for displaying a specific user profile.

    This view retrieves a Profile object based on the provided username and
    passes it to the 'profiles/profile.html' template.
    It is used to display detailed information about a specific user profile.

    Args:
        request: The HttpRequest object.
        username (str): The username of the user whose profile is to
        be retrieved.

    Returns:
        HttpResponse: The rendered page for the specified user profile.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
