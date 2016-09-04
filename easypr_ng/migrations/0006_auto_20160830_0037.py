# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easypr_ng', '0005_auto_20160828_1440'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='content',
            new_name='post_body',
        ),
        migrations.AddField(
            model_name='publication',
            name='assigned_to',
            field=models.ForeignKey(related_name='Third_party_Editor', default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='publication',
            name='platform',
            field=models.ForeignKey(default='', verbose_name=b'Media platform', to='easypr_ng.MediaPlatform'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='sector',
            field=models.ForeignKey(default='', verbose_name=b'Media sector', to='easypr_ng.Sector'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publication',
            name='press_material',
            field=models.ForeignKey(verbose_name=b'Media category', to='easypr_ng.PressMaterial'),
        ),
    ]
