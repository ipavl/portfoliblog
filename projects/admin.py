from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    """
    Behaviour specific to the Django admin panel.
    """
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin)