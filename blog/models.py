from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from  datetime import datetime
from django.http import request
# Create your models here.
from django.urls import reverse


class Category(models.Model):
    category =models.CharField(max_length=256)
    def __str__(self):
        return self.category


    class Meta:
        verbose_name_plural = "Blog Categories"




class Blog(models.Model):


    title=models.CharField(max_length=256)
    short_description=models.CharField(max_length=256)
    article=RichTextField()
    article_thumbnail=CloudinaryField('Maximum of 1')
    country=models.CharField(max_length=256)
    city=models.CharField(max_length=256)
    posted_date=models.DateTimeField(auto_now_add=True)
    posted_by=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=256)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=(str(self.pk)))

    class Meta:
        verbose_name_plural = "Blog Posts"
        ordering = ['-posted_date']




class FeaturedPosts(models.Model):
    title = models.CharField(max_length=256)
    short_description = models.CharField(max_length=256)
    article = RichTextField()
    article_thumbnail = CloudinaryField('Maximum of 1')
    country = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    posted_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=256)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Featured Posts"
        ordering = ['-posted_date']
        get_latest_by='posted_date'

    def get_absolute_url(self):
        return reverse('post', args=(str(self.pk)))


