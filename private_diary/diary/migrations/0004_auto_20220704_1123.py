# Generated by Django 3.2.5 on 2022-07-04 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_diary_conclude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='conclude',
        ),
        migrations.AddField(
            model_name='diary',
            name='conclude_text',
            field=models.TextField(blank=True, verbose_name='まとめテキスト'),
        ),
        migrations.AddField(
            model_name='diary',
            name='conclude_title',
            field=models.TextField(blank=True, verbose_name='まとめタイトル'),
        ),
    ]
