from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
from django.urls import reverse


class PastorsQuote(models.Model):
    title = models.CharField(max_length=256)
    short_description = models.CharField(max_length=256)
    pastors_quote = RichTextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pastors_picture=CloudinaryField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Pastors Quote"
        ordering = ['-posted_date']

    def get_absolute_url(self):
        return reverse('post', args=(str(self.pk)))




class Grid(models.Model):
    image=CloudinaryField('Maximum of 1')
    posted_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Grid Images"
        ordering = ['-posted_date']

    def get_absolute_url(self):
        return reverse('post', args=(str(self.pk)))



