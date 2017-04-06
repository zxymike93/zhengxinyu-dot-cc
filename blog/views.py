from django.shortcuts import render, get_object_or_404

from .models import Blog


def list(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/list.html', context={'blogs': blogs})


def detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/detail.html', context={'blog': blog})

