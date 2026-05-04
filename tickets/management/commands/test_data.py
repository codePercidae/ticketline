"""The structure of this file is mostly gotten from Claude sonnet 4.6.
Implementation is still a work of the repos owner."""

from django.core.management.base import BaseCommand
from tickets.models import User, Event

class Command(BaseCommand):
    help = "Resets or creates the test data for application."

    def handle(self, *args, **kwargs):
        test_users = [
            {"username" : "esim", "password" : "1234", "balance" : 200, "admin" : False},
            {"username" : "exmpl", "password" : "4321", "balance" : 200, "admin" : False},
            {"username" : "admin", "password" : "admin", "balance" : 0, "admin" : True},
        ]
    
        test_events = [
            {"name" : "Some random gig in your local pub", "price" : 75},
            {"name" : "Taalor Swooftie in some crazy big stadion", "price": 5999}
        ]

        for user in test_users:
            user, created = User.objects.update_or_create(
                username = user["username"],
                defaults = user
            )
            print("Created or updated test user : " , user)
        
        for event in test_events:
            event, created = Event.objects.update_or_create(
                name = event["name"],
                defaults=event
            )
            print("Created or updated test event: " , event)