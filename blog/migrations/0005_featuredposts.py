# Generated by Django 3.1.3 on 2020-12-16 10:39

import ckeditor.fields
import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20201216_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('short_description', models.CharField(max_length=256)),
                ('article', ckeditor.fields.RichTextField()),
                ('article_thumbnail', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Maximum of 1')),
                ('country', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(max_length=256)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Featured Posts',
            },
        ),
    ]
