from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    """
    Behaviour specific to the Django admin panel for the Post class.
    """
    prepopulated_fields = {'slug': ('title',)}
    exclude = ['date']

class CategoryAdmin(admin.ModelAdmin):
    """
    Behaviour specific to the Django admin panel for the Category class.
    """
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
