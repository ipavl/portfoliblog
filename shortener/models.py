from django.db import models

class ShortUrl(models.Model):
    """
    Represents a short URL.
    """
    name = models.CharField(
        max_length=200,
        unique=True,
        blank=False,
        help_text='Campaign display name for administrative identification.',
    )

    identifier = models.CharField(
        max_length=32,
        unique=True,
        blank=False,
        help_text='The actual short part of the URL, e.g. http://www.example.com/go/<strong>[identifier]</strong>.',
    )

    destination = models.URLField(
        max_length=2048,
        help_text='Where should the link go?',
        blank=False,
    )

    hits = models.BigIntegerField(
        default=0,
        editable=False,
    )

    def __str__(self):
        """
        How the entry will be shown in places such as Django admin.
        :return: The entry's name
        """
        return '%s' % self.name
