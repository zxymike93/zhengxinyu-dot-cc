from django import forms
from django.contrib import admin

from note.models import Note, NoteImage


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        widgets = {
            'content': forms.Textarea(attrs={'rows': 100, 'cols': 100}),
        }
        exclude = ['overview']
        # fields = ['title', 'content']


class NoteImageInline(admin.TabularInline):

    model = NoteImage
    extra = 0


class NoteAdmin(admin.ModelAdmin):

    form = NoteForm
    inlines = [NoteImageInline]


admin.site.register(Note, NoteAdmin)

# Register your models here.
