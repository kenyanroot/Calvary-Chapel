# Generated by Django 3.1.3 on 2020-12-16 07:55

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='article_picture',
            new_name='article_thumbnail',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='picture',
        ),
        migrations.AlterField(
            model_name='blog',
            name='article',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted_by',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]