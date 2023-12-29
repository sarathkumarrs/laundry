from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50,null=True)
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=50)

    def __str__(self) :
        return self.username
     


