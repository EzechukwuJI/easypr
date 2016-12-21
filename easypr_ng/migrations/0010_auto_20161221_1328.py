# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0009_auto_20161216_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='adv_duration',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='adv_service_type',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='audio_file',
            field=models.FileField(null=True, upload_to=b'uploads/audio/'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='media_house',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='page_color',
            field=models.CharField(blank=True, max_length=125, null=True, choices=[(b'black and white', b'black and white'), (b'color', b'color')]),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='page_size',
            field=models.CharField(default=None, max_length=125),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='region',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='video_file',
            field=models.FileField(null=True, upload_to=b'uploads/video/'),
        ),
        migrations.AlterField(
            model_name='publication',
            name='uploaded_text',
            field=models.FileField(null=True, upload_to=b'uploads/publication/%Y-%M-%D', blank=True),
        ),
        migrations.AlterField(
            model_name='publicationimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'uploads/images/publication', blank=True),
        ),
        migrations.AlterField(
            model_name='requestimage',
            name='image',
            field=models.ImageField(null=True, upload_to=b'uploads/images/request', blank=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='uploaded_post_content',
            field=models.FileField(upload_to=b'uploads/images/blogger_distribution/contents/'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='persons_image',
            field=models.FileField(upload_to=b'uploads/testimonial/images'),
        ),
    ]
