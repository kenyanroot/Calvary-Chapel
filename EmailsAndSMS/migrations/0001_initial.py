# Generated by Django 3.1.3 on 2020-12-23 09:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', ckeditor.fields.RichTextField()),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Emails',
            },
        ),
        migrations.CreateModel(
            name='EmailSubscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber', models.EmailField(max_length=54)),
            ],
            options={
                'verbose_name_plural': 'Email Subscribers',
            },
        ),
    ]
