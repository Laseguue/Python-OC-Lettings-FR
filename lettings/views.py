from django.shortcuts import render
from .models import Letting


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
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings/index.html', context)


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
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'lettings/letting.html', context)
