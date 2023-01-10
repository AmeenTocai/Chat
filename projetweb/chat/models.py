from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
