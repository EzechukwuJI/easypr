# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bouquet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=75, choices=[(b'Single', b'Single'), (b'Basic', b'Basic'), (b'Maxi', b'Maxi'), (b'Super Maxi', b'Super Maxi')])),
                ('name_slug', models.CharField(max_length=75)),
                ('price_per_media_N', models.FloatField(default=0.0, verbose_name=b'Price in Naira')),
                ('price_per_media_D', models.FloatField(default=0.0, verbose_name=b'Price in Dollar')),
                ('discounted_price_per_media_N', models.FloatField(default=0.0, verbose_name=b'Discounted Price Naira')),
                ('discounted_price_per_media_D', models.FloatField(default=0.0, verbose_name=b'Discounted Price Dollar')),
                ('num_of_media', models.IntegerField(default=0)),
                ('percentage_commission', models.FloatField(default=0.0)),
                ('percentage_savings', models.FloatField(default=0.0)),
                ('amount_payable_N', models.FloatField(default=0.0, verbose_name=b'Total amount in Naira')),
                ('amount_payable_D', models.FloatField(default=0.0, verbose_name=b'Total amount in Dollar')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(max_length=1000)),
                ('website', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='CommentReply',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('reply', models.TextField(max_length=1000)),
                ('comment', models.ForeignKey(to='easypr_ng.Comment')),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MediaContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=125)),
                ('last_name', models.CharField(max_length=125)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('email', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='MediaHouse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('name_slug', models.CharField(max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('contact_persons', models.ManyToManyField(to='easypr_ng.MediaContact', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaPlatform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('name_slug', models.CharField(max_length=75)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PayDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=25, null=True)),
                ('payment_method', models.CharField(default=b'', max_length=75, choices=[(b'Bank Deposit', b'Bank Deposit'), (b'Card Payment', b'Card Payment'), (b'Bank Transfer', b'Bank Transfer')])),
                ('amount_paid', models.FloatField(default=0.0)),
                ('date_paid', models.CharField(max_length=100, null=True, blank=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True, choices=[(b'Diamond Bank', b'Diamond Bank'), (b'GTB', b'GTB')])),
                ('teller_number', models.CharField(max_length=15, null=True, blank=True)),
                ('pay_status', models.CharField(default=b'pending', max_length=25, choices=[(b'verified', b'verified'), (b'pending', b'pending'), (b'failed', b'failed')])),
                ('verified_by', models.BooleanField(default=False)),
                ('date_verified', models.DateTimeField(null=True, blank=True)),
                ('user', models.ForeignKey(verbose_name=b'Payment By', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PressMaterial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_slug', models.CharField(max_length=150)),
                ('media_type', models.CharField(max_length=150)),
                ('price_per', models.FloatField(default=0.0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=15)),
                ('post_title', models.CharField(max_length=175)),
                ('title_slug', models.CharField(max_length=200)),
                ('status', models.CharField(default=b'New', max_length=50, choices=[(b'New', b'New'), (b'sent_to_external_editor', b'sent_to_external_editor'), (b'Processing', b'Processing'), (b'Published', b'Published'), (b'Rejected', b'Rejected')])),
                ('post_body', models.TextField(max_length=3000, null=True, blank=True)),
                ('person_to_quote', models.CharField(max_length=125, null=True, blank=True)),
                ('persons_position', models.CharField(max_length=125, null=True, blank=True)),
                ('uploaded_text', models.FileField(null=True, upload_to=b'publication/%Y-%M-%D', blank=True)),
                ('date_published', models.DateTimeField(null=True, blank=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('publish_online', models.BooleanField(default=False, verbose_name=b'Do you also want online publication of the chosen media? ')),
                ('completed', models.BooleanField(default=False)),
                ('assigned_to', models.ForeignKey(related_name='Third_party_Editor', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('media_houses', models.ManyToManyField(to='easypr_ng.MediaHouse')),
                ('platform', models.ForeignKey(verbose_name=b'Media platform', blank=True, to='easypr_ng.MediaPlatform', null=True)),
                ('posted_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('press_material', models.ForeignKey(verbose_name=b'Media category', blank=True, to='easypr_ng.PressMaterial', null=True)),
                ('published_by', models.ForeignKey(related_name='Edited_and_published_by', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicationImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(null=True, upload_to=b'publicaton_image/%Y/%M/%D', blank=True)),
                ('caption', models.CharField(max_length=200, null=True, blank=True)),
                ('post', models.ForeignKey(blank=True, to='easypr_ng.Publication', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=15)),
                ('deleted', models.BooleanField(default=False)),
                ('ordered', models.BooleanField(default=False)),
                ('status', models.CharField(default=b'New', max_length=75, choices=[(b'New', b'New'), (b'Processing', b'Processing'), (b'Pending', b'Pending'), (b'Rejected', b'Rejected'), (b'Closed', b'Closed')])),
                ('date_purchased', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Redirect_url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=None, max_length=200, null=True, blank=True)),
                ('post', models.ForeignKey(blank=True, to='easypr_ng.Publication', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('name_slug', models.CharField(max_length=75)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseInvoice',
            fields=[
                ('purchase_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='easypr_ng.Purchase')),
                ('receipt_no', models.CharField(max_length=12)),
                ('invoice', models.FileField(null=True, upload_to=b'Invoices/%Y-%M-%D', blank=True)),
            ],
            bases=('easypr_ng.purchase',),
        ),
        migrations.AddField(
            model_name='purchase',
            name='bouquet',
            field=models.ForeignKey(to='easypr_ng.Bouquet'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='payment_details',
            field=models.ForeignKey(default=None, verbose_name=b'Payment details', to='easypr_ng.PayDetails'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='publication',
            field=models.OneToOneField(to='easypr_ng.Publication'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(verbose_name=b'Purchased By', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publication',
            name='sector',
            field=models.ForeignKey(verbose_name=b'Media sector', blank=True, to='easypr_ng.Sector', null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='site',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='mediahouse',
            name='platform',
            field=models.ManyToManyField(to='easypr_ng.MediaPlatform', blank=True),
        ),
        migrations.AddField(
            model_name='mediacontact',
            name='media_house',
            field=models.ForeignKey(to='easypr_ng.MediaHouse'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='easypr_ng.Publication'),
        ),
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='media_houses',
            field=models.ManyToManyField(to='easypr_ng.MediaHouse'),
        ),
        migrations.AddField(
            model_name='bouquet',
            name='press_material',
            field=models.ForeignKey(to='easypr_ng.PressMaterial'),
        ),
    ]
