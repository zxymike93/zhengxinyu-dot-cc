from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from unidecode import unidecode


class CommonInfo(models.Model):

    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(CommonInfo):

    name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Note(CommonInfo):

    category = models.ForeignKey(Category, null=True)
    title = models.CharField(max_length=150, unique=True)
    subtitle = models.CharField(max_length=150)
    content = models.TextField()
    slug = models.SlugField(max_length=200, blank=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return 'id: {}\ntitle:{}\n'.format(self.id, self.title)

    def overview(self):
        return self.content[:50]

    def save(self):
        self.slug = slugify(unidecode(self.title))
        super().save()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug': self.slug})


class NoteImage(models.Model):

    note = models.ForeignKey(Note)
    image = models.ImageField(upload_to='note/')
