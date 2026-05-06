from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    balance = models.IntegerField()
    admin = models.BooleanField()

    def __str__(self):
        return f"User {self.username}, password: {self.password}, balance: {self.balance}, admin: {self.admin}"

class Event(models.Model):
    name = models.CharField()
    price = models.IntegerField()

    def __str__(self):
        return f"Event {self.name}, price: {self.price}"
    
'''This probably should also have some other fields in order to
actually help the security measures'''
class Security_log(models.Model):
    username = models.CharField()
    password = models.CharField()
    success = models.BooleanField()
