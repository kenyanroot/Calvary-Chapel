# Generated by Django 3.1.3 on 2020-12-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('picture', models.CharField(max_length=256)),
                ('short_description', models.CharField(max_length=256)),
                ('article', models.CharField(max_length=256)),
                ('article_picture', models.CharField(max_length=256)),
                ('country', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('posted_date', models.CharField(max_length=256)),
                ('posted_by', models.CharField(max_length=256)),
                ('category', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Blog Posts',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name_plural': 'Blog Categories',
            },
        ),
    ]
