from django import forms
from django.contrib import admin

from .models import Blog, BlogImage


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        widgets = {
            'content': forms.Textarea(attrs={'rows': 100, 'cols': 100}),
        }
        exclude = ['overview']
        # fields = ['title', 'content']


class BlogImageInline(admin.TabularInline):

    model = BlogImage
    extra = 0


class BlogAdmin(admin.ModelAdmin):

    form = BlogForm
    inlines = [BlogImageInline]


admin.site.register(Blog, BlogAdmin)
