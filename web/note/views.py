from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from note.models import Note, Category


def list(request, category):
    if category:
        category = get_object_or_404(Category, name=category)
        all_notes = category.note_set.filter(
            publish=True).order_by('-update_time')
    else:
        all_notes = Note.objects.filter(publish=True).order_by('-update_time')

    """
    page = request.GET.get('page')
    paginator = Paginator(all_notes, 1)
    try:
        notes = paginator.page(page)
    except PageNotAnInteger:
        notes = paginator.page(1)
    except EmptyPage:
        notes = paginator.page(paginator.num_pages)
    """
    notes = all_notes

    context = {
        'notes': notes,
        'categories': Category.objects.all()
    }

    return render(request, 'note/list.html', context=context)


def detail(request, slug):
    note = get_object_or_404(Note, slug=slug)
    return render(request, 'note/detail.html', context={'note': note})
