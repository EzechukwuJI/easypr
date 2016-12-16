# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0006_auto_20161209_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='blog_list',
            field=models.ManyToManyField(to='easypr_ng.Blogs'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='post_content',
            field=models.TextField(default='', max_length=3000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='total_price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='uploaded_post_content',
            field=models.FileField(default='', upload_to=b'images/blogger_distribution/contents/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogs',
            name='category',
            field=models.CharField(max_length=125, choices=[(b'top-blogs', b'Top Blogs'), (b'technology', b'Technology')]),
        ),
        migrations.AlterField(
            model_name='publicationimage',
            name='image',
            field=models.FileField(null=True, upload_to=b'images/publication/%Y/%M/%D', blank=True),
        ),
        migrations.AlterField(
            model_name='requestimage',
            name='image',
            field=models.FileField(null=True, upload_to=b'images/request/%Y/%M/%D', blank=True),
        ),
    ]
