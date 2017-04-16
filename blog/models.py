from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from unidecode import unidecode


class Blog(models.Model):
    
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=150)
    content = models.TextField()
    slug = models.SlugField(max_length=200, blank=True)
    category = models.CharField(max_length=30, blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return 'id: {}\ntitle:{}\n'.format(self.id, self.title)

    def overview(self):
        return self.content[:50]

    def save(self):
        self.slug = slugify(unidecode(self.title))
        super().save()

    def blog_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class BlogImage(models.Model):

    blog = models.ForeignKey(Blog)
    image = models.ImageField(upload_to='blog/')
