from django.shortcuts import render
from core.models import Post, Category
import random
from django.core.paginator import Paginator

# Create your views here.

def core_index(request):
    p = Paginator(Post.objects.all().order_by("-created_on"), 27)
    page = request.GET.get('oldal')
    posts = p.get_page(page)
    context = {
        "posts": posts,
    }
    return render(request, "core/index.html", context)

def core_post(request, slug):
    post = Post.objects.get(slug=slug)
    news = Post.objects.all().exclude(pk=post.pk).order_by("-created_on")[:4]
    related_posts = list(Post.objects.filter(category=post.category, banner=True).exclude(pk=post.pk))
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
    p = Paginator(Post.objects.filter(category=category), 10)
    page = request.GET.get('oldal')
    posts = p.get_page(page)
    context = {
        "posts": posts,
    }
    return render(request, "core/list.html", context)

def core_news(request):
    p = Paginator(Post.objects.all().order_by("-created_on"), 10)
    page = request.GET.get('oldal')
    posts = p.get_page(page)
    context = {
        "posts": posts,
    }
    return render(request, "core/list.html", context)