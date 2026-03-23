from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    balance = models.IntegerField()
    admin = models.BooleanField()

class Event(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    transactionfee = models.FloatField(db_default=2.5)
    extrafee = models.FloatField(db_default=5.0)
    extrafee2 = models.FloatField(db_default=4.5)
    extrafee3 = models.FloatField(db_default=150)
    extrafee4 = models.FloatField(db_default=0.5)