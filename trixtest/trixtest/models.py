from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()

