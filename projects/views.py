from django.shortcuts import render
from projects.models import Project

def index(request):
    projects = Project.objects.order_by("-date")
    return render(request, 'projects/index.html', {"projects": projects})
