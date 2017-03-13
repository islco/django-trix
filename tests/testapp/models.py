from django.db import models
from trix.fields import TrixField


class Post(models.Model):
    title = models.CharField(max_length=128)
    raw_content = models.TextField()
    rich_content = TrixField()
