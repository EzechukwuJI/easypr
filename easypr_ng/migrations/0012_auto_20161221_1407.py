# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0011_auto_20161221_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='adv_instructions',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='advert_image_file',
            field=models.FileField(help_text=b'for newpaper advert submission', null=True, upload_to=b'uploads/newspaper/advert'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='audio_file',
            field=models.FileField(help_text=b'for Radio advert submission', null=True, upload_to=b'uploads/audio/'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='page_size',
            field=models.CharField(max_length=125, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='uploaded_post_content',
            field=models.FileField(help_text=b'for blogger distibution submission', upload_to=b'uploads/images/blogger_distribution/contents/'),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='video_file',
            field=models.FileField(help_text=b'for TV advert submission', null=True, upload_to=b'uploads/video/'),
        ),
    ]
