from django.contrib import admin
from pages.models import Page

class PageAdmin(admin.ModelAdmin):
    """
    Behaviour specific to the Django admin panel.
    """
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Page, PageAdmin)
