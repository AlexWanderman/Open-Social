from random import choice

from django.contrib.auth import get_user_model
from django.db import models

from .folder import Folder

User = get_user_model()


def generate_link():
    i = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    for _ in range(10):
        link = ''.join([choice(i) for x in range(16)])

        if not File.objects.filter(link=link).exists():
            break
    else:
        raise ValueError('Не удалось сгенерировать ссылку')

    return link


class File(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    folder = models.ForeignKey(Folder, models.CASCADE, null=True)
    file = models.FileField(upload_to='')
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=50, unique=True, default=generate_link)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)


class SavedFile(models.Model):
    file = models.ForeignKey(File, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    # тот, кто сохранил себе


class ImageFile(models.Model):
    file = models.OneToOneField(File, models.CASCADE)
    about = models.CharField(max_length=500, null=True)


class ImageMention(models.Model):
    image = models.ForeignKey(ImageFile, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    # кого упомянули, упомянуть может только кто загрузил изображение


class VideoFile(models.Model):
    file = models.OneToOneField(File, models.CASCADE)
    about = models.CharField(max_length=500, null=True)
    # + изображение-предпросмотр (по желанию)


class VideoMention(models.Model):
    video = models.ForeignKey(VideoFile, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    # кого упомянули, упомянуть может только кто загрузил изображение


class MusicFile(models.Model):
    file = models.OneToOneField(File, models.CASCADE)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    lyrics = models.CharField(max_length=500, null=True)
    # + обложка (по желанию)


class PodcastFile(models.Model):
    file = models.OneToOneField(File, models.CASCADE)
    creator = models.CharField(max_length=50)
    theme = models.CharField(max_length=50)
    about = models.CharField(max_length=500, null=True)
    # + обложка (по желанию)


class DocumentFile(models.Model):
    file = models.OneToOneField(File, models.CASCADE)
    program = models.CharField(max_length=50, null=True)
    about = models.CharField(max_length=500, null=True)
