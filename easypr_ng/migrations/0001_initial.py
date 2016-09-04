# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('easypr_general', '0001_initial'),
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
                ('Num_of_media', models.IntegerField(default=0)),
                ('percentage_commission', models.FloatField(default=0.0)),
                ('amount_payable_N', models.FloatField(default=0.0, verbose_name=b'Total amount in Naira')),
                ('amount_payable_D', models.FloatField(default=0.0, verbose_name=b'Total amount in Dollar')),
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
                ('platform', models.CharField(max_length=25, choices=[(b'Newspaper', b'Newspaper'), (b'Blog', b'Blog')])),
                ('contact_persons', models.ManyToManyField(to='easypr_ng.MediaContact', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PayDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=25)),
                ('payment_method', models.CharField(max_length=75, choices=[(b'Bank Deposit', b'Bank Deposit'), (b'Card Payment', b'Card Payment'), (b'Bank Transfer', b'Bank Transfer')])),
                ('amount_paid', models.FloatField(default=0.0)),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True, choices=[(b'Diamond Bank', b'Diamond Bank'), (b'GTB', b'GTB')])),
                ('teller_number', models.CharField(max_length=15, null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
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
            name='PubDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('document', models.FileField(null=True, upload_to=b'publication/%Y-%M-%D', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_title', models.CharField(max_length=175)),
                ('title_slug', models.CharField(max_length=200)),
                ('status', models.CharField(default=b'new', max_length=50, choices=[(b'New', b'New'), (b'sent_to_external_editor', b'sent_to_external_editor'), (b'Processing', b'Processing'), (b'Published', b'Published'), (b'Rejected', b'Rejected')])),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=3000, null=True, blank=True)),
                ('person_to_quote', models.CharField(max_length=125, null=True, blank=True)),
                ('persons_position', models.CharField(max_length=125, null=True, blank=True)),
                ('pictures', models.FileField(null=True, upload_to=b'media/', blank=True)),
                ('uploaded_text', models.FileField(null=True, upload_to=b'publication/%Y-%M-%D', blank=True)),
                ('deleted', models.BooleanField(default=False)),
                ('publish_online', models.BooleanField(default=False, verbose_name=b'Do you also want online publication of the chosen media? ')),
                ('date_published', models.DateTimeField(null=True, blank=True)),
                ('media_houses', models.ManyToManyField(to='easypr_ng.MediaHouse')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transaction_id', models.CharField(max_length=15)),
                ('deleted', models.BooleanField(default=False)),
                ('ordered', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=75, choices=[(b'New', b'New'), (b'Processing', b'Processing'), (b'Pending', b'Pending'), (b'Rejected', b'Rejected'), (b'Closed', b'Closed')])),
                ('date_purchased', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Redirect_url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(default=None, max_length=200, null=True, blank=True)),
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
            field=models.ForeignKey(verbose_name=b'Payment details', to='easypr_ng.PayDetails'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='publication',
            field=models.ForeignKey(to='easypr_ng.Publication'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(verbose_name=b'Purchased By', to='easypr_general.UserAccount'),
        ),
        migrations.AddField(
            model_name='publication',
            name='media_urls',
            field=models.ManyToManyField(to='easypr_ng.Redirect_url'),
        ),
        migrations.AddField(
            model_name='publication',
            name='posted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publication',
            name='press_material',
            field=models.ForeignKey(to='easypr_ng.PressMaterial'),
        ),
        migrations.AddField(
            model_name='publication',
            name='published_by',
            field=models.ForeignKey(related_name='Edited_and_published_by', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='site',
            field=models.ManyToManyField(to='sites.Site'),
        ),
        migrations.AddField(
            model_name='pubdocument',
            name='publication',
            field=models.OneToOneField(null=True, blank=True, to='easypr_ng.Publication', verbose_name=b'Related publication'),
        ),
        migrations.AddField(
            model_name='mediacontact',
            name='media_house',
            field=models.ForeignKey(to='easypr_ng.MediaHouse'),
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
