What are Django signals?

Django signals allow certain actions to be taken when certain events 
occur in a Django application. They are used to allow certain parts
of the application to get notified when certain actions occur elsewhere
in the application.

Why are Django signals important?

Django signals are a useful tool for allowing certain parts of the application
to be notified of changes or actions taken elsewhere in the application.
This can be especially useful when working with a large application with
many different components that need to be able to communicate with each other.

For example, let's say you have a Django application that allows users to create 
and edit articles. When a user creates a new article, you might want to send an 
email notification to the site administrators. You could use a Django signal to 
send this notification every time a new article is created.

How do you implement Django signals?

To use Django signals, you first need to import the signals module from Django.
Next, you'll need to define the signal that you want to use.
This is done using the @receiver decorator.

Here's an example of how to implement a signal that sends an email notification 
every time a new article is created:

from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Article)
def send_notification_email(sender, instance, **kwargs):
    send_mail(
        'New Article Created',
        'A new article has been created: {}'.format(instance.title),
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )


In this example, the send_notification_email function is the signal's callback function.
It will be called every time a new article is created. The post_save signal is triggered 
every time an object is saved to the database, so this signal will be called whenever a
new article is created or an existing article is updated.






