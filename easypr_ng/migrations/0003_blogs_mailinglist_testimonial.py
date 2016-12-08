# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0002_auto_20161205_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name_slug', models.CharField(max_length=275)),
                ('category', models.CharField(max_length=125, choices=[(b'Top_blogs', b'Top_blogs'), (b'Technology', b'technology')])),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=165)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.CharField(max_length=150)),
                ('persons_position', models.CharField(max_length=75)),
                ('persons_company', models.CharField(max_length=125)),
                ('persons_image', models.FileField(upload_to=b'testimonial/images')),
            ],
        ),
    ]
