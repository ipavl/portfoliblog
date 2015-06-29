from django.db import models
from django.db.models import permalink

class Project(models.Model):
    """
    Represents an individual project.
    """
    name = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='Text to be shown in the URL for this item. Auto-populates based on the name field.',
    )

    date = models.DateField(
        help_text='e.g. the date the project was started or first made publicly available.',
    )

    project_url = models.URLField(
        blank=True,
        help_text='Link to project homepage or "project overview" style pages.',
    )

    demo_url = models.URLField(
        blank=True,
        help_text='Link to somewhere the user can try the project out.',
    )

    source_url = models.URLField(
        blank=True,
        help_text='Link to public Git repo, etc.',
    )

    image = models.ImageField(
        blank=True,
        upload_to='',
        help_text='Logo or screenshot. Requires Pillow to be installed.',
    )

    technologies = models.CharField(
        max_length=200,
        help_text='List what the project was built with here.',
    )

    description = models.TextField(
        help_text='Describe what the project does. You may use Markdown.',
    )

    def __str__(self):
        """
        How the project will be shown in places such as Django admin.
        :return: The project's name
        """
        return '%s' % self.name

    @permalink
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('views.view_project', args=[str(self.slug)])
