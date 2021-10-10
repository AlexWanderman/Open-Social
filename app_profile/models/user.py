from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # username   - [a-zA-Z0-9]{3,33}
    # password
    # first_name - [a-zA-Zа-яёА-ЯЁ]{2,20}
    # last_name  - [a-zA-Zа-яёА-ЯЁ]{2,20}
    # name       - [a-zA-Z0-9]{3,33}

    name = models.CharField(max_length=20, unique=True)
    about = models.TextField()
    birthday = models.DateField()
