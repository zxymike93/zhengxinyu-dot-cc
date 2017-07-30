# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-30 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('subtitle', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('category', models.CharField(blank=True, max_length=30)),
                ('publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='NoteImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='note/')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='note.Note')),
            ],
        ),
    ]
