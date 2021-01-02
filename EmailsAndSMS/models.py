from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.




class EmailSubscribers(models.Model):
    subscriber=models.EmailField(max_length=54)

    class Meta:
        verbose_name_plural = "Email Subscribers"



class Emails(models.Model):
    email=RichTextField()
    time_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Emails"

