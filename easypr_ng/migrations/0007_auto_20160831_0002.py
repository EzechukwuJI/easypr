# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0006_auto_20160830_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='assigned_to',
            field=models.ForeignKey(related_name='Third_party_Editor', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='platform',
            field=models.ForeignKey(verbose_name=b'Media platform', blank=True, to='easypr_ng.MediaPlatform', null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='press_material',
            field=models.ForeignKey(verbose_name=b'Media category', blank=True, to='easypr_ng.PressMaterial', null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='sector',
            field=models.ForeignKey(verbose_name=b'Media sector', blank=True, to='easypr_ng.Sector', null=True),
        ),
    ]
