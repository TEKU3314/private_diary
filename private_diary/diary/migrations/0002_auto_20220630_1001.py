# Generated by Django 3.2.5 on 2022-06-30 01:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='content',
        ),
        migrations.AddField(
            model_name='diary',
            name='content1',
            field=models.TextField(blank=True, null=True, verbose_name='本文1'),
        ),
        migrations.AddField(
            model_name='diary',
            name='content2',
            field=models.TextField(blank=True, null=True, verbose_name='本文２'),
        ),
        migrations.AddField(
            model_name='diary',
            name='content3',
            field=models.TextField(blank=True, null=True, verbose_name='本文３'),
        ),
        migrations.AddField(
            model_name='diary',
            name='content4',
            field=models.TextField(blank=True, null=True, verbose_name='本文４'),
        ),
        migrations.AddField(
            model_name='diary',
            name='content5',
            field=models.TextField(blank=True, null=True, verbose_name='本文５'),
        ),
        migrations.AddField(
            model_name='diary',
            name='item1',
            field=models.TextField(blank=True, verbose_name='項目１'),
        ),
        migrations.AddField(
            model_name='diary',
            name='item2',
            field=models.TextField(blank=True, verbose_name='項目２'),
        ),
        migrations.AddField(
            model_name='diary',
            name='item3',
            field=models.TextField(blank=True, verbose_name='項目３'),
        ),
        migrations.AddField(
            model_name='diary',
            name='item4',
            field=models.TextField(blank=True, verbose_name='項目４'),
        ),
        migrations.AddField(
            model_name='diary',
            name='item5',
            field=models.TextField(blank=True, verbose_name='項目５'),
        ),
        migrations.AddField(
            model_name='diary',
            name='photo4',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真４'),
        ),
        migrations.AddField(
            model_name='diary',
            name='photo5',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='写真５'),
        ),
        migrations.AddField(
            model_name='diary',
            name='subtitle',
            field=models.CharField(default=datetime.datetime(2022, 6, 30, 1, 1, 29, 396132, tzinfo=utc), max_length=100, verbose_name='サブタイトル'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diary',
            name='title_photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='タイトル写真'),
        ),
    ]
