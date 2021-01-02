from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    profile_picture = CloudinaryField('image')
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse('profile', args=(str(self.id)))

    def __str__(self):
        return self.user



