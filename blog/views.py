from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Blog


def list(request, page='1'):
    page = int(page)
    blogs = Blog.objects.all().order_by('-update_time')
    p = Paginator(blogs, 7).page(page)

    context = {
        'blogs': p.object_list,
        'next': p.next_page_number() if p.has_next() else None,
        'previous': p.previous_page_number() if p.has_previous() else None,
    }

    return render(request, 'blog/list.html', context=context)


def detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/detail.html', context={'blog': blog})

