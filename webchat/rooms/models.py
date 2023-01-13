from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True)

class Message(models.Model):
    user=models.ForeignKey(User,related_name='message',on_delete=models.CASCADE)
    text=models.TextField()
    room=models.ForeignKey(Room,related_name='message',on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

    class Order:
        ordering=('date',)