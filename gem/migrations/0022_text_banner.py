# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-08 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0074_banner_subtitle'),
        ('gem', '0021_commentcountrule'),
    ]

    operations = [
        migrations.CreateModel(
            name='GemTextBanner',
            fields=[
                ('bannerpage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.BannerPage')),
                ('hide_on_freebasics', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.bannerpage',),
        ),
        migrations.AlterField(
            model_name='gemuserprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[(b'f', 'female'), (b'm', 'male'), (b'-', "don't want to answer")], max_length=1, null=True),
        ),
    ]
