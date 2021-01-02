from django.contrib import admin

# Register your models here.
from .models import Emails,EmailSubscribers



class Email(admin.ModelAdmin):

    list_display = ['email', 'time_created']
admin.site.register(Emails,Email)



class EmailSubscriber(admin.ModelAdmin):

    list_display = ['subscriber']
admin.site.register(EmailSubscribers,EmailSubscriber)
