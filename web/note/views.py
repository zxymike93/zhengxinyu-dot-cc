from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from note.models import Note


def list(request, page='1'):
    print('note list')
    page = int(page)
    notes = Note.objects.all().order_by('-update_time')
    p = Paginator(notes, 7).page(page)

    context = {
        'notes': p.object_list,
        'next': p.next_page_number() if p.has_next() else None,
        'previous': p.previous_page_number() if p.has_previous() else None,
    }

    return render(request, 'note/list.html', context=context)


def detail(request, slug):
    note = get_object_or_404(Note, slug=slug)
    return render(request, 'note/detail.html', context={'note': note})
