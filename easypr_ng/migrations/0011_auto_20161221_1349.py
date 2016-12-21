# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0010_auto_20161221_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='adv_instructions',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='advert_image_file',
            field=models.FileField(null=True, upload_to=b'uploads/newspaper/advert'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='allow_content_editing',
            field=models.BooleanField(default=True, help_text=b'for newpaper advert submission'),
        ),
    ]
