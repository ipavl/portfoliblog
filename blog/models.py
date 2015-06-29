from django.db import models
from django.db.models import permalink

class Post(models.Model):
    title = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        help_text='Text to be shown in the URL for this item. Auto-populates based on the title field.',
    )

    date = models.DateTimeField(
        auto_now_add=True,
    )

    category = models.ForeignKey(
        'blog.Category',
        default='uncategorized',
    )

    body = models.TextField(
        help_text='Write your post content here. You may use Markdown.',
    )

    def __str__(self):
        """
        How the post will be shown in places such as Django admin.
        :return: The post's title
        """
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('views.view_blog_post', args=[str(self.slug)])

class Category(models.Model):
    name = models.CharField(
        max_length=32,
        unique=True,
    )

    slug = models.SlugField(
        max_length=32,
        unique=True,
    )

    class Meta:
        """
        Class-specific metadata.
        """
        verbose_name_plural = "categories"

    def __str__(self):
        """
        How the slug will be shown in places such as Django admin.
        :return: The category name
        """
        return '%s' % self.name

    @permalink
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('views.view_blog_post', args=[str(self.slug)])
