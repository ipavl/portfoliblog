from django.db.models import F
from django.shortcuts import redirect
from .models import ShortUrl

def goto(request):
    """
    Increments the hits counter for this URL and redirects the user to the full URL via a 301 redirect.
    """
    slug = request.path.split('/')[-1]

    # Get the destination
    destination = ShortUrl.objects.values('destination').get(identifier=slug).get('destination')

    # Increment the hits count
    # TODO: See why this only works once
    ShortUrl.objects.filter(identifier=slug).update(hits=F('hits') + 1)

    # Perform 301 redirect
    return redirect(destination, permanent=True)
