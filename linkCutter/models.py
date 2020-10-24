from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Link(models.Model):

    destination_link = models.URLField(max_length=255)
    source_link = models.SlugField(max_length=255, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.source_link

    def get_absolute_url(self):
        return reverse('user-link', kwargs={'slug': self.source_link})
