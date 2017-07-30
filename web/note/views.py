from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from note.models import Note


def list(request):
    all_notes = Note.objects.filter(publish=True).order_by('-update_time')
    paginator = Paginator(all_notes, 1)

    page = request.GET.get('page')
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)

    return render(request, 'note/list.html', {'notes': notes})


def detail(request, slug):
    note = get_object_or_404(Note, slug=slug)
    return render(request, 'note/detail.html', context={'note': note})
