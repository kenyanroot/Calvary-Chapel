from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from sendgrid import Mail, SendGridAPIClient

from EmailsAndSMS.models import Emails, EmailSubscribers
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        print('user created')


post_save.connect(create_profile,sender=User)


@receiver(post_save,sender=Emails)
def email_sender(sender,instance,**kwargs):


    Email_subscribers = EmailSubscribers.objects.all()




    msg = Emails.objects.latest('email')



    ms = msg.email






    for email_subscriber in Email_subscribers:
        email = email_subscriber.email








        message = Mail(
            from_email='anaclate@sky-swift.com',
            to_emails=email,
            subject='Newsletter subscription',
            html_content=ms,

        )

        try:
            sg = SendGridAPIClient('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')
            response = sg.send(message)
            # print(response.status_code)
            # print(response.body)
            # print(response.headers)

        except Exception as e:
            print('not working')


post_save.connect(email_sender,sender=Emails)







