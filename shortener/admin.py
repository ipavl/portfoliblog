from django.contrib import admin
from .models import ShortUrl

class ShortUrlAdmin(admin.ModelAdmin):
    """
    Behaviour specific to the Django admin panel for the ShortUrl class.
    """
    readonly_fields = ('hits',)

admin.site.register(ShortUrl, ShortUrlAdmin)
