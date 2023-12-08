import logging
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Letting


logger = logging.getLogger(__name__)


def index(request):
    """
    View for the index page of lettings.

    This view retrieves all Letting objects from the database and passes them
    to the 'lettings/index.html' template.
    It is typically used to display a list of all lettings available in
    the system.

    Args:
        request: The HttpRequest object.

    Returns:
        HttpResponse: The rendered index page with the list of lettings.
    """
    try:
        logger.info("Affichage de la page d'index des lettings")
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings/index.html', context)
    except Exception as e:
        logger.error(
            f"Erreur lors de l'affichage de l'index des lettings: {e}"
            )
        raise


def letting(request, letting_id):
    """
    View for displaying a specific letting.

    This view retrieves a Letting object based on the provided letting_id and
    passes it to the 'lettings/letting.html' template.
    It is used to display detailed information about a specific letting.

    Args:
        request: The HttpRequest object.
        letting_id (int): The ID of the letting to retrieve.

    Returns:
        HttpResponse: The rendered page for the specified letting.
    """
    try:
        letting = get_object_or_404(Letting, id=letting_id)
        logger.info(f"Affichage des détails du letting: {letting.title}")
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'lettings/letting.html', context)
    except Http404:
        logger.error(f"Le letting avec l'ID {letting_id} n'a pas été trouvé")
        raise
    except Exception as e:
        logger.error(f"Erreur lors de l'affichage des détails du letting: {e}")
        raise
