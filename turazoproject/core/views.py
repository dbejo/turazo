from django.shortcuts import render
from core.models import Post

# Create your views here.

def core_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "core/index.html", context)

def core_post(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        "post": post,
    }
    return render(request, "core/post.html", context)