from django.shortcuts import render, render_to_response, get_object_or_404
from projects.models import Project

def index(request):
    projects = Project.objects.order_by("-date")
    return render(request, 'projects/index.html', {"projects": projects})

def view_project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render_to_response('projects/details.html', {"project": project})
