from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    points = models.models.IntegerField(defautl=0)

    def __str__(self):
        return self.username