from django.shortcuts import render


def index(request):
    """
    View for the main index page of the application.

    This view renders the 'index.html' template. It's typically used as the
    landing page of the application.
    Since no context is passed to the template, it simply renders the static
    content of 'index.html'.

    Args:
        request: The HttpRequest object.

    Returns:
        HttpResponse: The rendered index page.
    """
    return render(request, 'index.html')
