from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100)

class Message(models.Model):
    value = models.CharField(max_length=1000)
    time = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.CharField(max_length=50)
    room = models.CharField(max_length=100)
