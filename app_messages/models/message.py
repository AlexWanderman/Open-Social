from django.db import models

from .stream import Stream
from .streamer import Streamer


class Message(models.Model):
    ''' Сообщение в потоке'''
    stream = models.ForeignKey(Stream, models.CASCADE)
    streamer = models.ForeignKey(Streamer, models.CASCADE)
    text = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)
