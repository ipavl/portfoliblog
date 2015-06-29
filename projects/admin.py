from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
    """
    Create the URL slug in the form based off of the project name.
    """
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Project, ProjectAdmin)