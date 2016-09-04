# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0007_auto_20160831_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paydetails',
            name='payment_method',
            field=models.CharField(default=b'', max_length=75, choices=[(b'Bank Deposit', b'Bank Deposit'), (b'Card Payment', b'Card Payment'), (b'Bank Transfer', b'Bank Transfer')]),
        ),
        migrations.AlterField(
            model_name='paydetails',
            name='transaction_id',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='status',
            field=models.CharField(default=b'New', max_length=50, choices=[(b'New', b'New'), (b'sent_to_external_editor', b'sent_to_external_editor'), (b'Processing', b'Processing'), (b'Published', b'Published'), (b'Rejected', b'Rejected')]),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='payment_details',
            field=models.ForeignKey(default=None, verbose_name=b'Payment details', to='easypr_ng.PayDetails'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='status',
            field=models.CharField(default=b'New', max_length=75, choices=[(b'New', b'New'), (b'Processing', b'Processing'), (b'Pending', b'Pending'), (b'Rejected', b'Rejected'), (b'Closed', b'Closed')]),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(verbose_name=b'Purchased By', to=settings.AUTH_USER_MODEL),
        ),
    ]
