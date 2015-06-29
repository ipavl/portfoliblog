from django.shortcuts import render
from blog.models import Post, Category

def index(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'blog/index.html', {"posts": posts})
