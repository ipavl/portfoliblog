from django.shortcuts import render

def index(request):
    return render(request, 'common/index.md')

def about(request):
    return render(request, 'common/about.md')
