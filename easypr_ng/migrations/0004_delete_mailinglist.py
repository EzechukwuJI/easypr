# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0003_blogs_mailinglist_testimonial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MailingList',
        ),
    ]
