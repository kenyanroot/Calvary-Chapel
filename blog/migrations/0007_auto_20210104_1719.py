# Generated by Django 3.1.3 on 2021-01-04 14:19

import ckeditor.fields
import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20201222_1230'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-posted_date'], 'verbose_name_plural': 'Blog Posts'},
        ),
        migrations.CreateModel(
            name='PastorsQuote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('short_description', models.CharField(max_length=256)),
                ('pastors_quote', ckeditor.fields.RichTextField()),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('pastors_picture', cloudinary.models.CloudinaryField(max_length=255)),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Pastors Quote',
                'ordering': ['-posted_date'],
            },
        ),
    ]
