from django.db import models

# Create your models here.
class Room(models.Model):
    name = models. CharField(max_length=50)
    state = models. CharField(max_length=50)
    timestamp = models. CharField(max_length=50)
    pin = models. CharField(max_length=5)

class Door(models.Model):
    name = models. CharField(max_length=50)
    state = models. CharField(max_length=50)
    timestamp = models. CharField(max_length=50)
    pin = models. CharField(max_length=5)