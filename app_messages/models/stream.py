from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Stream(models.Model):
    '''Поток сообщений'''
    types = (
        (0, 'Заметки'),
        (1, 'Диалог'),
        (2, 'Беседа'),
        (3, 'Рассылка'),
        (4, 'Бот'),
    )

    type = models.IntegerField(choices=types)
    owner = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    about = models.CharField(max_length=255, null=True)
