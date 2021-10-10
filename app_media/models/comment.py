from django.contrib.auth import get_user_model
from django.db import models

from .folder import Folder
from .file import File

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    text = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now=True)


class FolderComment(models.Model):
    folder = models.ForeignKey(Folder, models.CASCADE)
    comment = models.OneToOneField(Comment, models.CASCADE)


class FileComment(models.Model):
    file = models.ForeignKey(File, models.CASCADE)
    comment = models.OneToOneField(Comment, models.CASCADE)
