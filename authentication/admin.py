from django.contrib import admin

# Register your models here.
from .models import Profile



class Profiles(admin.ModelAdmin):

    list_display = ('user','first_name','last_name','profile_picture','email','phone_number')
admin.site.register(Profile,Profiles)

