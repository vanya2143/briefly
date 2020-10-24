from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.CharField(max_length=20, default='123')

    def __str__(self):
        return f'Профайл пользователя {self.user.username}'
