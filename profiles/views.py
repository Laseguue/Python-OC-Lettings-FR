import logging
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Profile

logger = logging.getLogger(__name__)


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
    try:
        logger.info("Affichage de la page d'index des profils")
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles/index.html', context)
    except Exception as e:
        logger.error(f"Erreur lors de l'affichage de l'index des profils: {e}")
        raise


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
    try:
        profile = get_object_or_404(Profile, user__username=username)
        logger.info(f"Affichage des détails du profil: {username}")
        context = {'profile': profile}
        return render(request, 'profiles/profile.html', context)
    except Http404:
        logger.error(
            f"Le profil avec le username {username} n'a pas été trouvé"
            )
        raise
    except Exception as e:
        logger.error(f"Erreur lors de l'affichage des détails du profil: {e}")
        raise
