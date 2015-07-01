from django.shortcuts import render, render_to_response, get_object_or_404
from blog.models import Post, Category

def index(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'blog/index.html', {"posts": posts})

def view_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render_to_response('blog/post.html', {"post": post})