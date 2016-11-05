# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easypr_ng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, choices=[(b'basic', b'Basic'), (b'regular', b'Regular'), (b'premium', b'Premium'), (b'premium-plus', b'Premium Plus')])),
                ('media_outreach_credit', models.CharField(default=1, max_length=25)),
                ('online', models.CharField(max_length=5, verbose_name=b'online_newspaper_publishing', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('monitoring', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('free_consulting', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('newsroom', models.CharField(max_length=5, verbose_name=b'Newsroom via EasyPR Media Desk', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('google_news_inclusions', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('reuters_news_network', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('hyperlinks', models.CharField(max_length=5, verbose_name=b'hyperlinks in online press release')),
                ('notification', models.CharField(max_length=5, verbose_name=b'publication notification via email', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('autopost', models.CharField(max_length=5, verbose_name=b'autopost to social media account', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('analytics', models.CharField(max_length=5, verbose_name=b'detailed analytics report', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('expedited', models.CharField(max_length=5, verbose_name=b'expedited release processing', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('available_on_homepage', models.CharField(max_length=5, verbose_name=b'news made available to journalists, bloggers and researchers via EasyPR homepage', choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('content_writing', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('content_editing', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('featured_package', models.CharField(max_length=5, choices=[(b'yes', b'yes'), (b'no', b'no')])),
                ('price_naira', models.FloatField(default=0.0, max_length=25)),
                ('price_dollar', models.FloatField(default=0.0, max_length=25)),
                ('active', models.BooleanField(default=False)),
                ('is_promo', models.BooleanField(default=False)),
                ('promo_starts', models.DateTimeField(auto_now_add=True)),
                ('promo_ends', models.DateTimeField(auto_now_add=True)),
                ('promo_price_dollar', models.FloatField(default=0.0, max_length=25)),
                ('promo_price_naira', models.FloatField(default=0.0, max_length=25)),
                ('category', models.ForeignKey(to='easypr_ng.PressMaterial')),
            ],
            options={
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.RemoveField(
            model_name='packages',
            name='category',
        ),
        migrations.AlterField(
            model_name='purchase',
            name='package',
            field=models.ForeignKey(to='easypr_ng.Package'),
        ),
        migrations.DeleteModel(
            name='Packages',
        ),
    ]
