from django.db import models
from django.db.models import permalink

class Page(models.Model):
    """
    Represents an individual page.
    """
    title = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='Text to be shown in the URL for this item. Auto-populates based on the name field.',
    )

    content = models.TextField(
        help_text='The content to display on the page. You may use Markdown.',
    )

    show_in_menu = models.BooleanField(
        help_text='If checked, will display this page as a link in the main site navigation.',
    )

    def __str__(self):
        """
        How the page will be shown in places such as Django admin.
        :return: The page's title
        """
        return '%s' % self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('view_page', args=[str(self.slug)])
