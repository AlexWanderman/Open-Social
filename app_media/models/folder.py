from random import choice

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def generate_link():
    i = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    for _ in range(10):
        link = ''.join([choice(i) for x in range(16)])

        if not Folder.objects.filter(link=link).exists():
            break
    else:
        raise ValueError('Не удалось сгенерировать ссылку')

    return link


class Folder(models.Model):
    # cover - опциональная обложка
    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=500)
    link = models.CharField(max_length=50, unique=True, default=generate_link)


class SavedFolder(models.Model):
    folder = models.ForeignKey(Folder, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    # тот, кто сохранил себе


class ImageFolder(models.Model):
    folder = models.OneToOneField(Folder, models.CASCADE)


class VideoFolder(models.Model):
    folder = models.OneToOneField(Folder, models.CASCADE)


class MusicFolder(models.Model):
    folder = models.OneToOneField(Folder, models.CASCADE)


class PodcastFolder(models.Model):
    folder = models.OneToOneField(Folder, models.CASCADE)


class DocumentFolder(models.Model):
    folder = models.OneToOneField(Folder, models.CASCADE)
