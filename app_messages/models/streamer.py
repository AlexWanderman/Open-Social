from django.contrib.auth import get_user_model
from django.db import models

from .stream import Stream

User = get_user_model()


class Streamer(models.Model):
    '''Участник общения с его правами'''
    stream = models.ForeignKey(Stream, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    can_write = models.BooleanField()
