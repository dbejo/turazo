from django.shortcuts import render
from core.models import Post, Category
import random

# Create your views here.

def core_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "core/index.html", context)

def core_post(request, slug):
    post = Post.objects.get(slug=slug)
    news = Post.objects.all().order_by("-created_on")[:4]
    related_posts = list(Post.objects.filter(category=post.category, banner=True))
    if len(related_posts) < 6 :
        random_related_posts = random.sample(related_posts, len(related_posts))
    else:
        random_related_posts = random.sample(related_posts, 6)
    context = {
        "post": post,
        "news": news,
        "related_posts": random_related_posts
    }
    return render(request, "core/post.html", context)

def core_categories(request, slug):
    category = Category.objects.get(slug=slug)
    posts = Post.objects.filter(category=category)
    context = {
        "posts": posts,
    }
    return render(request, "core/list.html", context)