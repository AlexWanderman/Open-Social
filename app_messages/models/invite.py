from random import choice

from django.db import models

from .stream import Stream


def generate_link():
    i = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    for _ in range(10):
        link = ''.join([choice(i) for x in range(16)])

        if not Invite.objects.filter(link=link).exists():
            break
    else:
        raise ValueError('Не удалось сгенерировать ссылку')

    return link


class Invite(models.Model):
    stream = models.ForeignKey(Stream, models.CASCADE)
    link = models.CharField(max_length=50, unique=True, default=generate_link)
    # права вступающих, ограничения на колво и время
