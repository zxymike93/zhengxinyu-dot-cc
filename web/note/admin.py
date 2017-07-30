from django import forms
from django.contrib import admin

from note.models import Note, NoteImage, Category


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


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Note, NoteAdmin)
admin.site.register(Category, CategoryAdmin)
