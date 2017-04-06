from django import forms
from django.contrib import admin

from .models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        widgets = {
            'content': forms.Textarea(attrs={'rows': 100, 'cols': 100}),
        }
        exclude = ['overview']
        # fields = ['title', 'content']


class BlogAdmin(admin.ModelAdmin):

    form = BlogForm


admin.site.register(Blog, BlogAdmin)

